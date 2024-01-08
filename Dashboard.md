---
cssclass: dashboard
banner: "![[Pasted image 20230814123307.png]]"
banner_y: 0.4345
---

# Habit Tracking
- ```tracker
searchType: frontMatter
searchTarget: gym
folder: Life/Journal/Daily Notes
datasetName: Gym
fixedScale: 0.75
month:
	mode: annotation
	annotation: 🏋️‍♂️
	startWeekOn: 'Mon'
	color: blue```
	
- ```tracker
searchType: frontMatter
searchTarget: morning-yoga
folder: Life/Journal/Daily Notes
datasetName: Morning Yoga
fixedScale: 0.75
month:
	mode: annotation
	annotation: 🌅
	startWeekOn: 'Mon'
	color: yellow```

- ```tracker
searchType: frontMatter
searchTarget: meditated
folder: Life/Journal/Daily Notes
datasetName: Meditation
fixedScale: 0.75
month:
	mode: annotation
	annotation: 🧘‍♂️
	startWeekOn: 'Mon'
	color: green```

- ```tracker
searchType: frontMatter
searchTarget: morning-vitamins
folder: Life/Journal/Daily Notes
datasetName: Morning Vitamins
fixedScale: 0.75
month:
	mode: annotation
	annotation: 💊
	startWeekOn: 'Mon'
	color: orange```

- ```tracker
searchType: frontMatter
searchTarget: evening-vitamins
folder: Life/Journal/Daily Notes
datasetName: Evening Vitamins
fixedScale: 0.75
month:
	mode: annotation
	annotation: 💊
	startWeekOn: 'Mon'
	color: purple```

- ```tracker
searchType: frontmatter
searchTarget: water
folder: Life/Journal/Daily Notes
fixedScale: 0.75
line:
	title: Water Log
	yAxisLabel: Water
	yAxisUnit: oz
	xAxisLabel: Date
	lineColor: blue```
	
- ```tracker
searchType: frontmatter
searchTarget: morning-mood, evening-mood
folder: Life/Journal/Daily Notes
datasetName: Morning, Evening
fixedScale: 0.75
line:
	title: Morning and Evening Mood
	yAxisLabel: Morning, Evening
	xAxisLabel: Date
	lineColor: yellow, red
	showLegend: true```

- ```tracker
searchType: frontmatter
searchTarget: energy
folder: Life/Journal/Daily Notes
fixedScale: 0.75
line:
	title: Energy Levels
	yAxisLabel: Energy
	xAxisLabel: Date
	lineColor: yellow```

- ```tracker
searchType: frontmatter
searchTarget: weight
folder: Life/Journal/Daily Notes
fixedScale: 0.75
line:
	title: Weight Log
	yAxisLabel: Weight
	yAxisUnit: Lbs
	xAxisLabel: Date
	lineColor: yellow```

- ```tracker
searchType: frontmatter
searchTarget: hours-to-wakeup
folder: Life/Journal/Daily Notes
fixedScale: 0.75
line:
	title: Sleep Log
	yAxisLabel: Time
	yAxisUnit: Hours
	xAxisLabel: Date
	lineColor: yellow```
# Personal Projects
- 📁 Portfolio 
	- Come up with some ideas loser

# Miravalis
- 🎲 Running

# School
- 📅 Scheduling
	- Look around for new classes

# Career
- 💻 Programming Team
	- Work on HackerRank Practice

# Vault Info

- 🗄️ Recent file updates `$=dv.list(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(4).file.link)`
- 🔖 Tagged: favorite `$=dv.list(dv.pages('#favorite').sort(f=>f.file.name,"desc").limit(4).file.link)`
- 〽️ Stats
    - File Count: `$=dv.pages().length`
    - Daily Journal Entries: `$=dv.pages('"Life/Journal/Daily Notes"').length`