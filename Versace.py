def plotWordDict(x, scale):
    ## x is of type dict, scale is to fit screen
    initbar = "\n"+"="*int((max(x.values())+35) / scale);
    print(initbar + "\nWord Frequency In Migos' 'Versace'" + initbar)
    [print("." * int(xx / scale), xx, "  (" + ww + ")") for ww, xx in x.items()]
    print(initbar)

song = "Versace, Versace, Medusa head on me like I'm 'Luminati I know that you like it, Versace, my neck and my wrist is so sloppy Versace, Versace, I love it, Versace the top of my Audi My plug, he John Gotti, he give me the ducks And I know that they're mighty Versace, Versace, Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace Versace, Versace, Medusa head on me like I'm 'Luminati I know that you like it, Versace, my neck and my wrist is so sloppy Versace, Versace, I love it, Versace the top of my Audi My plug, he John Gotti, he give me the ducks And I know that they're mighty Shoes and shirt Versace, your bitch want in on my pockets She ask me why my drawers silk, I told that bitch 'Versace' Cheetah print on my sleeve, but I ain't ever been in the jungle Try to take my sack, better run with it, n**** don't fumble Versace, Versace, Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace You can do Truey, I do Versace You copped the Honda, I copped the Mazi You smoke the mid, I smoke exotic I set the trend, you n****s copy Cooking the dope, like I work at Hibachi Lookin and watching, blow it, hot like some Taki Come in my room, my sheet Versace When i go to sleep, I dream Versace Medusa, Medusa, Medusa These n****s, they wishing they knew ya They coppin' the Truey, remixing the Louie My blunts is fat as Rasputia In a striped shirt like I'm Tony the Tiger I'm beating the pot, Call me Michael Lot of you n****s they copy Look at my closet Versace, Versace Versace, Versace, Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace King of Versace, Medusa my wifey My car is Versace, tiger stripes on my Mazi I'm dressing so nice, they can't even copy You think I'm Egyptian, this gold on my body My money my mission, two bitches they kissing My diamonds is pissy, my swag is exquisite Young Offset no preacher, but you n****s listen Them blue and white diamonds dey look like the Pistons Codeine sippin, Versace I'm gripping them bands in my pocket You know that I'm living I'm draped up in gold but no Pharaoh Rockin' handcuffs, that's Ferragamo Bricks by the boat, overload I'm think I'm the don, but no Rocko This the life that I chose Bought out the store can't go back no more Versace my clothes, while I'm sellin them bows Versace took over, it took out my soul Versace, Versace, Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace, Versace, Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace, Versace Versace Versace, Versace Versace"
song = song.lower().replace(",", "").replace("'versace'", "versace").split()

counts = dict()  # keys are words, values are word counts
for word in song:
    if word in counts.keys():
        counts[word] += 1
    else:
        counts[word] = 1
        
sorteditems = sorted(counts.items(), key=lambda item: item[1]);
sorteditems.reverse();
plotWordDict(dict(sorteditems), 2)
