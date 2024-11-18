# Welcome to Web Development, Stinkers
![[Pasted image 20240211172242.png]]

---

- HTML - 4.33, CSS - 3.33
- JS - 4
- Components - 2.33
- State - 3
- Client/Server - 3.66
- Web APIs - 3.33
- Dynamic Routing - 2
- Metadata - 3.66
- Serverless - 2.66
- SEO - 2.66
- JSX - 2.66
- Node/npm/npx - 3
- Databases - 4, Storage Buckets - 2.33

---

- HTML - 4.33, JS - 4
- Databases - 4
- Client/Server - 3.66
- Metadata - 3.66
- CSS - 3.33
- Web APIs - 3.33
- State - 3
- Node/npm/npx - 3
- Serverless - 2.66
- SEO - 2.66
- JSX - 2.66
- Components - 2.33
- Storage Buckets - 2.33, Dynamic Routing - 2 ​

---
### Implementation Confidence
I get the feeling we're a little "back-end" brained here.

- JS - 4.33
- HTML - 2.66
- CSS - 2.33
- React - 2.33
- Tailwind - 2.33

---

### Outline
1. Building a site
2. Tools to make the site solve a problem, and intermediate steps
3. Deployment

---

### The Basics of building a site
A noob website consists of main 3 elements in implementation - HTML, CSS, and JavaScript. At the end of the day, most of the tools are simply supersets and extensions of these three that make development easier and more impactful.
- JSX = HTML++
- Tailwind = CSS++
- React = JavaScript++
- (Disclaimer: Giga-simplification)

---

### HTML
- HTML: Hypertext Markup Language
- A series of nested elements to represent a website structure
- Different attributes that serve for differing behavior
- Redundant in some cases...

---
![[Pasted image 20240211174503.png]]
---

![[Pasted image 20240211174433.png]]

---

### JSX
- The prodigal lovechild born from HTML and JavaScript
- Functional HTML flows and limiting redundancy
- Literally Js in HTML...

---

![[Pasted image 20240211174757.png]]

---

![[Pasted image 20240211175550.png]]

---

### Whats with the long ass class names?
- Tailwind is an extremely powerful CSS extension
- Compiled, and intellisense supported
- Adds element-level style system, which is incredibly powerful
- Universal measurement system - enforces consistency
- Allows for utility overrides
- Extensive documentation and manual - DW

---

![[Pasted image 20240211175852.png]]

---

![[Pasted image 20240211175931.png]]

---

![[Pasted image 20240211180123.png]]

---

![[Pasted image 20240211180344.png]]

---

### The elephant in the room
- React is what is called a JavaScript framework, or a way to extend Js for responsive user interfaces.
- Is responsible for managing state and rendering conditionally, based on changes in certain conditions/variables.

---

### Component Based Architecture
- React delegates JSX and Js functionality in components, which are reusable pieces that build our UI
- Each component returns JSX, and contains all of the functionality inside of itself, making these components standalone and reusable
- Components can receive inputs, also known as properties/props

QUESTION: ASK ABOUT BUCKET STORAGE / QR CODES

---

![[Pasted image 20240211182506.png]]

---

### Not so fast...
- We need to talk about TypeScript. It is a superset of JavaScript, so all of your prior knowledge is 100% valid. 
- Typescript adds is a layer of consistency and error checking by adding types to Js, and the option to create advanced types.
```Js
// Entity types are defined elsewhere...
type EntityItem = {
    value:
        | Character
        | City
        | Faction
        | Quest
        | Building;
    label: string;
};
```
---

![[Pasted image 20240211182801.png]]


---

### useState()
- The useState function returns two items - one is the stateful piece of data itself, and the other is the setter. You also input the default value into the call to useState, and specify the states the type.
- Any JSX element that uses stateful data as input will automatically be re-rendered

---

![[Pasted image 20240211181605.png]]

---

### useEffect()
- The useEffect function is called whenever stateful data changes 
- Has something called a dependency array, which we used to tell it what stateful data is allowed to execute it. (An empty dependency array only calls the useEffect once, also called the "on-mount" effect)
- Has a return function, which is called when the component is dismounted (leaves screen)

---

![[Pasted image 20240211181907.png]]

---

![[Pasted image 20240211182217.png]]

---

### Last piece of information... for now
- Next Js is what is known as a meta framework, and does a lot of the very complicated tasks under the hood
- Dynamic routing, or displaying a unique page given the website URL (https://www.projectwildspace.tech/dashboard/clrzq4phg0003uk6mrdg8e4ly)
- Setting metadata to improve your ability to come up on google search (SEO)
- Optimizing images and **Server Side Rendering**

---
### What is Server Side Rendering?
- First we need to understand the difference between Client and Server.
- CLIENT: what runs in the web browser. All of the useEffect and useState hooks are client functionality, since there are no fancy animations in the server until it hits the browser.
- SERVER: where your site is hosted, and what sends you the website when you navigate to the URL.

---

### Why is Server Side Rendering Good?
- Think about packaging the entire site and sending it to the client... slow load times, and time is money!
- Search Engine Optimization - if important portions of our site are already rendered, then that content will be in search engines, and thus, give the internet more chances to find the site

---

### Server Components in Action
![[Pasted image 20240211183458.png]]

---

### When to SSR (Server Side Rendering)
- When the data in the component is STATIC, and does not change from the UI. This does not include calls to databases, these can be done in server components.
- Informative Sections that do not need to care about state management and UI changes. 
- THE MORE SERVER THE BETTER! Best practice to break out stateful components into a smaller component, and use client in there.

---

### "Use client" and "Use server"
- By default, Next assumes all components are server components.
- If you need a client component, simply put ```"use client"``` at the top of the component 
![[Pasted image 20240211183858.png]]

---

### Getting started...
- Have ESLint, Prettier, Pretty Typescript Errors, and Tailwind CSS IntelliSense VSCode plugins. I also recommend vscode-icons, because file organization in web-dev is MESSY.
- Make sure you have node installed.
- Run ```npx create-next-app``` in your terminal and follow the instructions

---

![[Pasted image 20240211184221.png]]

---

![[Pasted image 20240211184246.png]]

---

![[Pasted image 20240211184347.png]]

---

### Boot it up...
- Run ```npm run dev``` in the terminal and your computer will serve the site on localhost:3000

---

![[Pasted image 20240211184529.png]]

---

### Fuck around with the syntax
- Make a portfolio site using Next, React, and Tailwind
- Make each section (About, Contact, Education, etc) a component.
- For listed sections, make each item its own component and map them using JSX. For example, a projects component has an array of objects representing projects, each with a title, description, and tag, Map those into a project component, which takes in the properties and returns a list element.
- Use the Tailwind Manual and server components!!!

--- 
### Final remarks until we dig in...
- TRPC - a way to manage api calls with typesafety and efficiency
- Prisma - a tool to interact with our databases
- Vercel - a platform that deploys any Next.js app for FREE (with limits)
