---

---
# Welcome back, time for tools
On the agenda for today
- tRPC, database and repository initializing, prisma, t3 stack, and auth
- Collaboration tools
- App design
---
### API Handling
- Why do we care about tRPC? What problem does it fix

```js
import type { NextApiRequest, NextApiResponse } from 'next' 

type ResponseData = { message: string} 

export default function handler( 
	req: NextApiRequest, 
	res: NextApiResponse<ResponseData>) {
	res.status(200).json({ message: 'Hello from Next.js!' })
}
```

---
### A few issues
- Notice how we have to create a type
- We need to define status messages
- The type is known in the API, but what about in the client?
- Would we need to create and export a global type for all of our API returns, and import them to every client code that calls this API?
- Classic POST, UPDATE, CREATE, DELETE headers (verbose)
---
### tRPC, and what is so cracked
- Creates global typing across the entire project at development time
- Adds autocomplete for all API routes, and inputs, creating a "Project Based SDK"
- Reduces the need for request headers on the client side as they are inferred server side, and reduced to mutation and query
- Makes API management feel a lot more like functions (input and outputs versus req and res), than the classic HTTPS payload system

---
### tRPC Procedures

```js
// Middleware sneak peak...
getUserWorlds: privateProcedure.query(async ({ ctx }) => {
	const { userId } = ctx;

	// Prisma sneak peek...
	return await db.world.findMany({
		where: {
			userId,
		},
	});
}),
```

---
### Calling it Client Side

```js
export default function IndexPage() {
const result = trpc.greeting.useQuery({ name: 'client' });

	if (!result.data) {
	return (
	<div style={styles}>
		<h1>Loading...</h1>
	</div>
	);
	}
	
	return (
	<div style={styles}>
		<h1>{result.data.text}</h1>
	</div>
	);
}
```
---
### Better error handling
- Any functional/interpretive errors will be automatically thrown as a 400 error code
- Error codes can be caught directly on the client end of the procedure requests
---

```js
const {
data: imageResponse,
refetch: imageFetch,
error: imageError,
} = trpc.generateImage.useQuery(
{ object: response, type: "City/Town" },
{ enabled: false } // Does not fetch on mount
);

// Tells the user if there is an error with request
useEffect(() => {
	if (imageError) {
		toast({
		title: "Error",
		description: `${imageError.message}`,
		variant: "destructive",
		});
		setLoading(false);
		return;
	}
}, [imageError, toast]);
```

---
### Amazing API Flow
- Allows you to call the following functions on a procedure call, which augment the flow of data even more:
- onMutate/onQuery - Gets executed immediately when the query/mutation is called
- onSucess - Gets executed once the API logic completes without error
- onSettled - Gets executed at the end, regardless of the outcome

---

```js
const { mutate: saveCity, error: saveError } = trpc.saveCity.useMutation({
	// If we were able to save the city, let the user know!
	onSuccess: () => {
		utils.getWorldEntities.invalidate();
		toast({
			title: "City Saved",
			description: "Your city has been saved.",
		});
	},
	// Call once we start the procedure in order to let our loader know it should spin
	onMutate: () => {
		setCurrentlySavingCity(true);
	},
	// Stop the loading state, regardless of success or failure
	onSettled() {
		setCurrentlySavingCity(false);
	},
	// Exists, but does not have access to the error code, so is not as good for UX or debug
	onError() {
	}
});
```

---
### Middleware
- We can also add functionality between our server and client with trpc middleware

```js
const middleware = t.middleware;

const isAuth = middleware(async (opts) => {
	const { getUser } = getKindeServerSession();
	const user = await getUser();
	if (!user?.id || !user?.email) {
		throw new TRPCError({ code: "UNAUTHORIZED", message: "Unauthorized" });
	}
	return opts.next({
		ctx: {
			userId: user.id,
			user,
		},
	}),
});

export const privateProcedure = t.procedure.use(isAuth);
```

---
### Cached and Invalidation
- The data from tRPC is CACHED per session, even across routes and components
- This makes our APIs very efficient, but we still have flow in case we want to force a refetch elsewhere

```js
const { mutate: deleteWorld } = trpc.deleteWorld.useMutation({
	// If the world deletion succeeds...
	onSuccess: () => {
		// Lets invalidate our cache for the getUserWorlds response, updating our dashboards and wherever else getUserWorlds has already given data to
		utils.getUserWorlds.invalidate();
	},
	onMutate: ({ id }) => {
		setCurrentlyDeletingWorld(id);
	},
	onSettled() {
		setCurrentlyDeletingWorld(null);
	},
});
```
---
### Prisma
- ORM: Object Relational Mapper
- Automatically creates types for us based on our database tables
- Allows for a universal syntax, regardless of the database used, and feels consistent with JavaScript conventions (no syntax whiplash)
- No more chunky SQL

---

```js
getUserWorlds: privateProcedure.query(async ({ ctx }) => {
	const { userId } = ctx;  
		return await db.world.findMany({	
			where: {		
				userId,
			},
	});
}),
```

---

```js
import {
	Building,
	Character,
	City,
	Faction,
	Item,
	Monster,
	Quest,
	Spell
} from "@prisma/client";
```

---
### Database
- I am thinking a SQL instance on PlanetScale for development, and perhaps we can get fancy and create an instance elsewhere once we are done

---
### Auth Provider
- My vote is for Clerk, it is an Authentication provider that allows us to let users signin with multiple socials, so they do not need to make a new account
- Gives excellent tooling for development and gives access to session details in the client and server for authentication flows
- 10,000 free monthly users

---
### T3 Stack...
- A build tool that automatically does all of the boiler plate for tRPC, Next, and Prisma
- Clerk would be implemented manually, but T3 and Clerk are partnered and there is excellent documentation for doing so
- This will let us focus on our app as time is quickly running out

---
### Hosting
- Linode, as it turns out, is a bit expensive for the project we are using. We get $100 free credits, which we could use for launch month, and then cancel it after that. 

---

### Our core server driver... the Bun Shell!
https://bun.sh/blog/the-bun-shell#environment-variables-like-foo-bar-script-doesn-t-work-on-windows

---
### A little testing on my own...
Let me show you...

---
### Obsidian
- Let us set up an obsidian git-synced repository for collaboration on the project???
- Kanban Boards??? Whiteboards anyone???
---