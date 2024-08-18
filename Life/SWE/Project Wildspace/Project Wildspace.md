## Router Composition
1. Landing Page (projectwildspace.tech)
- Advertising for the product, generic landing page with testing etc. A sign-up and sign-in link.
- Sign in, sign out, authcallback 
1. Dashboard (/dashboard)
- Will display all of the worlds associated with each user.
- Displays the number of entities per world, and worlds per user, and summary.
- Allows deletion of a world (warning - deletes all entities within the world)
- Allows editing of a world (in a modal)
- Access to user settings
2. User Settings (/dashboard/settings)
- Allows you to manage your subscription and delete your account
3. World Page (/dashboard/[worldID])
- Displays the context of the world in a world tab
- Multiple Tabs for generation
- Gallery, NPC, Location, Organization, City, Country
	- The Gallery will display all entities in the world, and allow you to delete entities as well.
	- Each Generation Tab will have a text context prompt of up to 150 words, as well as each property of the entity. 
	- Each generated property of the entity can be overwritten by typing into the labels. By clicking the lock box next to each label, you can lock the field in generation.
	- A save button will be at the bottom of the generation, which will save that entity to the database.
	- A load button will also be at the bottom of each entity, allowing you to load in and edit an entity. Doing this deletes the old one from the database and creates a new entity, which will have the uploaded data.
	- A context button will allow the users to select up to 3 other entities to reference in the generation of the current entity. Perhaps using a Data Table
	- An image button will allow users to generate images for their generations, which will be displayed and saved as a URL.
4. Gallery Redirect (/dashboard/[worldID]/entityType/[entityID])
- Has a view of each of the entities in a readable format.

## Data Models

### User
```prisma
model User {
  id    String @id @unique //matches kinde user id
  email String @unique

  World    World[]

  stripeCustomerId       String?   @unique @map(name: "stripe_customer_id")
  stripeSubscriptionId   String?   @unique @map(name: "stripe_subscription_id")
  stripePriceId          String?   @map(name: "stripe_price_id")
  stripeCurrentPeriodEnd DateTime? @map(name: "stripe_current_period_end")
}
```

### World
```prisma
model World {
  id    String @id (@autoincrement)
  name String

  // World Attributes
  description String
  levelOfTech String
  levelOfMagic String
  currentYear Int

  // Arrays of entity types
}
```

