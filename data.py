print("Loading show data from static/data.py...")
SHOW =[
    {
  "reality_tv_shows": [
    {
      "id": 1,
      "title": "The Traitors",
      "season": 4,
      "network": "Peacock",
      "year": 2026,
      "premiere_date": "January 8, 2026",
      "host": "Alan Cumming",
      "notable_cast": [
        "Rob Rausch",
        "Lisa Rinna",
        "Maura Higgins",
        "Donna Kelce",
        "Porsha Williams",
        "Michael Rapaport",
        "Dorinda Medley",
        "Colton Underwood",
        "Monét X Change",
        "Johnny Weir",
        "Tara Lipinski"
      ],
      "rating": 5,
      "genre": ["competition", "mystery", "strategy"],
      "summary": "The Emmy Award-winning series returns for its most star-studded season yet, packing 23 celebrities into a hauntingly beautiful Scottish Highlands castle for the ultimate game of deception. A secret group of 'Traitors' — including a hidden 'Secret Traitor' wearing a red cloak — works to eliminate the loyal 'Faithfuls' through nightly murders, while the Faithfuls attempt to expose and banish the Traitors through dramatic roundtable votes. Season 4 introduces a wild new Secret Traitor twist: a fourth Traitor selected before the game even begins, who operates independently and doesn't know the other Traitors' identities. With Housewives, Olympians, Survivor legends, and pop culture icons all vying for $250,000, alliances shatter and no one is safe.",
      "episodes": 11,
      "status": "Airing",
      "similar_show_ids": [2, 3, 7],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/b/b7/The_Traitors_US_S4_poster.jpg",
        "alt": "Official promotional poster for The Traitors Season 4 on Peacock, featuring the 23-person celebrity cast dressed in elegant attire gathered inside the dimly lit Scottish Highlands castle, with Alan Cumming in a dramatic tartan suit at the center"
      }
    },
    {
      "id": 2,
      "title": "Survivor",
      "season": 46,
      "network": "CBS",
      "year": 2024,
      "premiere_date": "February 28, 2024",
      "host": "Jeff Probst",
      "notable_cast": [
        "Kenzie Petty",
        "Charlie Davis",
        "Maria Shrime Gonzalez",
        "Q Burdette",
        "Ben Katzman"
      ],
      "rating": 4,
      "genre": ["competition", "strategy", "survival"],
      "summary": "One of the longest-running reality competition shows in television history, Survivor drops a new group of castaways on a remote island where they must outwit, outplay, and outlast one another to claim the $1 million prize. Season 46 returns to the iconic Fijian islands, pushing contestants to their physical and mental limits through intense tribal challenges, blindsides, and social manipulation. Alliances shift constantly as players navigate the game's signature twists and tribal council eliminations.",
      "episodes": 13,
      "status": "Completed",
      "similar_show_ids": [1, 3, 5],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/9/96/Survivor46logo.png",
        "alt": "The Survivor Season 46 logo set against a tropical Fijian backdrop with the iconic torch and flame, representing the show's enduring theme of survival and competition"
      }
    },
    {
      "id": 3,
      "title": "Big Brother",
      "season": 26,
      "network": "CBS",
      "year": 2024,
      "premiere_date": "July 17, 2024",
      "host": "Julie Chen Moonves",
      "notable_cast": [
        "Chelsie Baham",
        "Rubina Bernabe",
        "Tucker Des Lauriers",
        "Makensy Manbeck",
        "Joseph Rodriguez"
      ],
      "rating": 4,
      "genre": ["competition", "strategy", "social experiment"],
      "summary": "Big Brother places a group of strangers together in a custom-built house outfitted with cameras in every room, broadcasting their every move 24/7. Contestants compete in Head of Household and Power of Veto competitions to gain safety and control nominations, while forming strategic alliances and social bonds. Each week, houseguests vote one of their own out of the house, until a final two or three face the jury for the $750,000 prize. Season 26 introduced an AI twist called 'AI Arena' that dramatically changed the power structure.",
      "episodes": 38,
      "status": "Completed",
      "similar_show_ids": [1, 2, 7],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/8/85/Big_Brother_Season_26.jpg",
        "alt": "The Big Brother Season 26 logo featuring the iconic eye motif in bold neon against a dark background, symbolizing constant surveillance inside the Big Brother house"
      }
    },
    {
      "id": 4,
      "title": "The Real Housewives of New York City",
      "season": 15,
      "network": "Bravo",
      "year": 2023,
      "premiere_date": "July 16, 2023",
      "host": "Andy Cohen",
      "notable_cast": [
        "Jessel Taank",
        "Erin Dana Lichy",
        "Ubah Hassan",
        "Sai De Silva",
        "Brynn Whitfield",
        "Jenna Lyons"
      ],
      "rating": 3,
      "genre": ["lifestyle", "drama", "docuseries"],
      "summary": "The rebooted 15th season of The Real Housewives of New York City follows a fresh ensemble of powerful, stylish New York women navigating friendship, business ventures, romance, and relentless drama across the city's most exclusive social circles. With an entirely new cast introduced for the reboot, viewers follow the women through glitzy events, shocking confrontations, and deeply personal revelations. The season culminates in a no-holds-barred reunion special where past feuds and unresolved conflicts collide.",
      "episodes": 18,
      "status": "Completed",
      "similar_show_ids": [6, 8, 10],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/0/07/RHONY_Season_15.jpg",
        "alt": "The Real Housewives of New York City Season 15 promotional image showing the new cast of women dressed glamorously against the Manhattan skyline at night"
      }
    },
    {
      "id": 5,
      "title": "The Amazing Race",
      "season": 36,
      "network": "CBS",
      "year": 2024,
      "premiere_date": "March 13, 2024",
      "host": "Phil Keoghan",
      "notable_cast": [
        "Derek Xiao",
        "Claire Rehfuss",
        "Juan Villa",
        "Shane Bilek",
        "Lena Wiedner"
      ],
      "rating": 4,
      "genre": ["competition", "travel", "adventure"],
      "summary": "Teams of two race across the globe, navigating foreign cultures, languages, and landscapes while completing physically demanding and mentally taxing challenges at each pit stop. The last team to check in at each leg risks elimination, while Express Passes and Speed Bumps add strategic layers to the competition. Season 36 takes racers through stunning destinations across four continents, testing relationships and individual resilience in equal measure. The first team to reach the final mat wins $1 million.",
      "episodes": 11,
      "status": "Completed",
      "similar_show_ids": [2, 3, 7],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/8/8d/The_Amazing_Race_Season_36_poster.jpg",
        "alt": "The Amazing Race Season 36 key art featuring racing teams mid-sprint against a colorful world map collage, capturing the global adventure and competitive energy of the show"
      }
    },
    {
      "id": 6,
      "title": "Vanderpump Rules",
      "season": 11,
      "network": "Bravo",
      "year": 2024,
      "premiere_date": "January 30, 2024",
      "host": "Andy Cohen",
      "notable_cast": [
        "Tom Sandoval",
        "Ariana Madix",
        "Tom Schwartz",
        "Katie Maloney",
        "Scheana Shay",
        "Lala Kent"
      ],
      "rating": 4,
      "genre": ["lifestyle", "drama", "docuseries"],
      "summary": "Set in the glitzy world of Lisa Vanderpump's West Hollywood restaurant empire, Vanderpump Rules follows the dramatic personal and professional lives of the SUR restaurant staff. Season 11 picks up in the aftermath of the explosive 'Scandoval' affair storyline that took over pop culture, continuing to follow Tom Sandoval and Ariana Madix's post-breakup dynamic alongside their group of longtime friends. New cast additions inject fresh drama as the veterans attempt to rebuild — or burn down — their relationships.",
      "episodes": 12,
      "status": "Completed",
      "similar_show_ids": [4, 8, 10],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/7/79/Vanderpump_Rules_title_card.jpg",
        "alt": "The Vanderpump Rules Season 11 promotional poster featuring the cast posed glamorously outside SUR restaurant in West Hollywood, with bold pink and gold typography"
      }
    },
    {
      "id": 7,
      "title": "The Mole",
      "season": 2,
      "network": "Netflix",
      "year": 2024,
      "premiere_date": "March 8, 2024",
      "host": "Alex Wagner",
      "notable_cast": [
        "Avori Henderson",
        "Casey Walker",
        "Greg Shapiro",
        "Jacob Hacker",
        "Melissa Roth"
      ],
      "rating": 4,
      "genre": ["competition", "mystery", "strategy"],
      "summary": "The Mole is a gripping mystery-competition hybrid in which contestants work together on missions to build a group prize pot — but one player secretly sabotages the group as 'The Mole.' Players must gather clues, suspect their teammates, and correctly identify The Mole to avoid elimination and ultimately win the prize. Netflix's revival of the classic early-2000s format brings back the paranoia-fueled gameplay with an updated cast of civilians navigating stunning international locations. Every alliance is suspect, and anyone could be deceiving the group.",
      "episodes": 10,
      "status": "Completed",
      "similar_show_ids": [1, 2, 3],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/5/57/The_Mole_2024_Netflix_poster.jpg",
        "alt": "Netflix's The Mole Season 2 promotional image featuring contestants in silhouette looking at a magnifying glass, representing the central mystery of identifying the saboteur among the group"
      }
    },
    {
      "id": 8,
      "title": "The Real Housewives of Atlanta",
      "season": 16,
      "network": "Bravo",
      "year": 2024,
      "premiere_date": "May 5, 2024",
      "host": "Andy Cohen",
      "notable_cast": [
        "Kenya Moore",
        "Kandi Burruss",
        "Shereé Whitfield",
        "Marlo Hampton",
        "Lisa Wu",
        "Courtney Rhodes"
      ],
      "rating": 3,
      "genre": ["lifestyle", "drama", "docuseries"],
      "summary": "The Real Housewives of Atlanta follows a group of fiercely independent and fabulously wealthy women living their best lives — and worst fights — in the heart of Atlanta. Season 16 reunites legacy cast members with fresh faces, delivering a season full of lavish parties, business drama, romantic entanglements, and the show's trademark explosive confrontations. Personal revelations and long-held grudges explode across both dramatic girls' trips and the iconic multi-part reunion hosted by Andy Cohen.",
      "episodes": 20,
      "status": "Completed",
      "similar_show_ids": [4, 6, 10],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/9/97/The_Real_Housewives_of_Atlanta_Season_16.jpg",
        "alt": "The Real Housewives of Atlanta Season 16 cast photo featuring the women in designer gowns posed against a dramatic Atlanta cityscape backdrop at golden hour"
      }
    },
    {
      "id": 9,
      "title": "Love Is Blind",
      "season": 7,
      "network": "Netflix",
      "year": 2024,
      "premiere_date": "October 2, 2024",
      "host": "Nick Lachey & Vanessa Lachey",
      "notable_cast": [
        "Hannah Jiles",
        "Nick Dorka",
        "Ramses Prashad",
        "Marissa George",
        "Stephen Nesbit",
        "Taylor Krause"
      ],
      "rating": 4,
      "genre": ["romance", "social experiment", "competition"],
      "summary": "Love Is Blind poses a radical question: can you fall in love with someone you've never seen? Contestants meet and date in isolated pods where they can only hear — never see — one another, and must decide whether to get engaged before ever laying eyes on their partner. Season 7 returns to Washington D.C., following couples as they navigate the real world together after engagement, meeting each other's families, and ultimately deciding at the altar whether to say 'I do' or walk away. Emotions run high as love, doubt, and social pressures collide.",
      "episodes": 11,
      "status": "Completed",
      "similar_show_ids": [4, 6, 10],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/4/4f/Love_Is_Blind_Season_7.jpg",
        "alt": "Love Is Blind Season 7 promotional image showing two silhouetted figures reaching toward each other through a glowing pod wall, representing the show's core concept of emotional connection without physical sight"
      }
    },
    {
      "id": 10,
      "title": "The Real Housewives of Dubai",
      "season": 2,
      "network": "Bravo",
      "year": 2024,
      "premiere_date": "June 2, 2024",
      "host": "Andy Cohen",
      "notable_cast": [
        "Chanel Ayan",
        "Caroline Brooks",
        "Nina Ali",
        "Sara Al Madani",
        "Caroline Stanbury",
        "Lesa Milan"
      ],
      "rating": 3,
      "genre": ["lifestyle", "drama", "docuseries"],
      "summary": "The Real Housewives of Dubai brings the iconic Housewives franchise to the world's most opulent city, following an international ensemble of powerhouse women who have made Dubai their home. Season 2 ramps up the glitz and drama, with the cast jetting between jaw-dropping mansions, world-class events, and exotic international destinations. Supermodel Chanel Ayan leads a cast that blends fierce ambition with genuine friendship — and bitter rivalries — against the backdrop of Dubai's extraordinary skyline and ultra-luxury lifestyle.",
      "episodes": 14,
      "status": "Completed",
      "similar_show_ids": [4, 6, 8],
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/en/7/74/Real_Housewives_of_Dubai_Season_2.jpg",
        "alt": "The Real Housewives of Dubai Season 2 cast standing in glamorous designer outfits against the Dubai skyline featuring the Burj Khalifa, showcasing the show's signature blend of luxury and international drama"
      }
    }
  ]
}
]