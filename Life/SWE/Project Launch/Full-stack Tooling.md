# Welcome back, time for tools
On the agenda for today
- tRPC, database and repository initializing, prisma, t3 stack, and auth
- Collaboration tools
- App design
---
### API Handling
- Why do we care about tRPC? What problem does it fix

![[Pasted image 20240229161607.png]]

---
### A few issues
- Notice how we have to create a type (ResponseData)
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
### Project Based SDK

![[Pasted image 20240229160227.png]]

---

![[Pasted image 20240229160559.png]]

---

![[Pasted image 20240229163854.png]]

---
![[Pasted image 20240229164000.png]]

---
### tRPC Procedures

![[Pasted image 20240229160759.png]]

---
### Calling it Client Side
![[Pasted image 20240229160945.png]]

---
### Better error handling
- Any functional/interpretive errors will be automatically thrown as a 400 error code
- Error codes can be caught directly on the client end of the procedure requests
---
![[Pasted image 20240229161018.png]]

---
### Amazing API Flow
- Allows you to call the following functions on a procedure call, which augment the flow of data even more:
- onMutate/onQuery - Gets executed immediately when the query/mutation is called
- onSucess - Gets executed once the API logic completes without error
- onSettled - Gets executed at the end, regardless of the outcome

---

![[Pasted image 20240229161107.png]]

---
### Middleware
- We can also add functionality between our server and client with trpc middleware

![[Pasted image 20240229161130.png]]

---

![[Pasted image 20240229163532.png]]

---
### Cached and Invalidation
- The data from tRPC is CACHED per session, even across routes and components
- This makes our APIs very efficient, but we still have flow in case we want to force a refetch elsewhere
---

![[Pasted image 20240229161212.png]]

---
### Prisma
- ORM: Object Relational Mapper
- Automatically creates types for us based on our database tables
- Allows for a universal syntax, regardless of the database used, and feels consistent with JavaScript conventions (no syntax whiplash)
- No more chunky SQL

---

![[Pasted image 20240229161304.png]]

---

![[Pasted image 20240229161336.png]]

---
### Database
- I am thinking a SQL instance on PlanetScale for development, and perhaps we can get fancy and create an instance elsewhere once we are done
---
### ShadCN UI!!!
- A installable component library
- Full styling and behavioral control
- Tailwind compliant
- Excellent variants
- Extremely ARIA performant

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