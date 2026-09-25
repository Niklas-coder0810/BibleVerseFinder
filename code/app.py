import streamlit as st
import random

st.set_page_config(page_title="VerseMatch", page_icon="✝️", layout="centered")

# Public-domain KJV passages. 120+ passages are included.
# The matching system uses broad themes rather than claiming to know exactly
# what a person feels.

VERSES = [
    # Fear / courage / protection
    ("Joshua 1:9", "Have not I commanded thee? Be strong and of a good courage; be not afraid, neither be thou dismayed: for the LORD thy God is with thee whithersoever thou goest.", ["fear","courage","hope","change"]),
    ("Isaiah 41:10", "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee.", ["fear","strength","hope","help"]),
    ("Deuteronomy 31:8", "And the LORD, he it is that doth go before thee; he will be with thee, he will not fail thee, neither forsake thee: fear not, neither be dismayed.", ["fear","courage","future","hope"]),
    ("Psalm 27:1", "The LORD is my light and my salvation; whom shall I fear? the LORD is the strength of my life; of whom shall I be afraid?", ["fear","courage","strength"]),
    ("Psalm 56:3", "What time I am afraid, I will trust in thee.", ["fear","trust","hope"]),
    ("Psalm 56:4", "In God I will praise his word, in God I have put my trust; I will not fear what flesh can do unto me.", ["fear","trust","courage"]),
    ("Psalm 34:4", "I sought the LORD, and he heard me, and delivered me from all my fears.", ["fear","help","hope"]),
    ("Psalm 34:7", "The angel of the LORD encampeth round about them that fear him, and delivereth them.", ["fear","protection","hope"]),
    ("Psalm 91:1", "He that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty.", ["fear","protection","peace"]),
    ("Psalm 91:4", "He shall cover thee with his feathers, and under his wings shalt thou trust.", ["fear","protection","trust"]),
    ("Psalm 118:6", "The LORD is on my side; I will not fear: what can man do unto me?", ["fear","courage","trust"]),
    ("Proverbs 3:25", "Be not afraid of sudden fear, neither of the desolation of the wicked, when it cometh.", ["fear","anxiety"]),
    ("2 Timothy 1:7", "For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.", ["fear","courage","love","strength"]),
    ("1 John 4:18", "There is no fear in love; but perfect love casteth out fear.", ["fear","love","peace"]),
    ("John 14:27", "Peace I leave with you, my peace I give unto you: let not your heart be troubled, neither let it be afraid.", ["fear","peace","anxiety"]),

    # Anxiety / worry / peace
    ("Philippians 4:6", "Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God.", ["anxiety","worry","prayer","gratitude"]),
    ("Philippians 4:7", "And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.", ["anxiety","peace","worry"]),
    ("1 Peter 5:7", "Casting all your care upon him; for he careth for you.", ["anxiety","worry","help","peace"]),
    ("Matthew 6:34", "Take therefore no thought for the morrow: for the morrow shall take thought for the things of itself.", ["worry","future","anxiety","peace"]),
    ("Matthew 6:25", "Therefore I say unto you, Take no thought for your life, what ye shall eat, or what ye shall drink.", ["worry","anxiety","trust"]),
    ("Matthew 11:28", "Come unto me, all ye that labour and are heavy laden, and I will give you rest.", ["stress","tired","overwhelmed","peace"]),
    ("Psalm 55:22", "Cast thy burden upon the LORD, and he shall sustain thee: he shall never suffer the righteous to be moved.", ["worry","stress","overwhelmed","help"]),
    ("Psalm 94:19", "In the multitude of my thoughts within me thy comforts delight my soul.", ["anxiety","worry","peace"]),
    ("Isaiah 26:3", "Thou wilt keep him in perfect peace, whose mind is stayed on thee: because he trusteth in thee.", ["anxiety","peace","trust"]),
    ("Psalm 4:8", "I will both lay me down in peace, and sleep: for thou, LORD, only makest me dwell in safety.", ["peace","sleep","worry","protection"]),
    ("Psalm 29:11", "The LORD will give strength unto his people; the LORD will bless his people with peace.", ["peace","strength","hope"]),
    ("Colossians 3:15", "And let the peace of God rule in your hearts, to the which also ye are called in one body; and be ye thankful.", ["peace","gratitude","anxiety"]),
    ("John 16:33", "These things I have spoken unto you, that in me ye might have peace. In the world ye shall have tribulation: but be of good cheer; I have overcome the world.", ["peace","hardship","hope","courage"]),
    ("Psalm 46:10", "Be still, and know that I am God.", ["peace","stress","trust"]),
    ("Exodus 14:14", "The LORD shall fight for you, and ye shall hold your peace.", ["stress","conflict","peace","trust"]),

    # Sadness / loneliness / comfort
    ("Psalm 34:18", "The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.", ["sadness","hurt","loneliness","comfort"]),
    ("Psalm 23:4", "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me.", ["sadness","fear","loneliness","hope"]),
    ("Psalm 147:3", "He healeth the broken in heart, and bindeth up their wounds.", ["sadness","hurt","comfort","hope"]),
    ("Psalm 42:11", "Why art thou cast down, O my soul? and why art thou disquieted within me? hope thou in God.", ["sadness","hope","loneliness"]),
    ("Psalm 30:5", "Weeping may endure for a night, but joy cometh in the morning.", ["sadness","hope","joy"]),
    ("Psalm 40:1", "I waited patiently for the LORD; and he inclined unto me, and heard my cry.", ["sadness","help","hope","patience"]),
    ("Psalm 61:2", "When my heart is overwhelmed: lead me to the rock that is higher than I.", ["sadness","overwhelmed","help","hope"]),
    ("Psalm 62:8", "Trust in him at all times; ye people, pour out your heart before him: God is a refuge for us.", ["sadness","trust","help","loneliness"]),
    ("Psalm 73:26", "My flesh and my heart faileth: but God is the strength of my heart, and my portion for ever.", ["sadness","strength","hope"]),
    ("Psalm 147:6", "The LORD lifteth up the meek: he casteth the wicked down to the ground.", ["sadness","hope","strength"]),
    ("Isaiah 43:2", "When thou passest through the waters, I will be with thee; and through the rivers, they shall not overflow thee.", ["sadness","fear","hardship","hope"]),
    ("Isaiah 49:15", "Can a woman forget her sucking child, that she should not have compassion on the son of her womb? yea, they may forget, yet will I not forget thee.", ["loneliness","sadness","hope"]),
    ("Matthew 5:4", "Blessed are they that mourn: for they shall be comforted.", ["sadness","loss","comfort"]),
    ("2 Corinthians 1:3", "Blessed be God, even the Father of our Lord Jesus Christ, the Father of mercies, and the God of all comfort.", ["sadness","comfort","hope"]),
    ("Revelation 21:4", "And God shall wipe away all tears from their eyes; and there shall be no more death, neither sorrow, nor crying.", ["sadness","loss","hope","comfort"]),

    # Hope / future / perseverance
    ("Jeremiah 29:11", "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.", ["hope","future","uncertainty"]),
    ("Romans 8:28", "And we know that all things work together for good to them that love God.", ["hope","hardship","future","trust"]),
    ("Romans 12:12", "Rejoicing in hope; patient in tribulation; continuing instant in prayer.", ["hope","hardship","patience","prayer"]),
    ("Romans 15:13", "Now the God of hope fill you with all joy and peace in believing, that ye may abound in hope.", ["hope","joy","peace","trust"]),
    ("Galatians 6:9", "And let us not be weary in well doing: for in due season we shall reap, if we faint not.", ["motivation","tired","perseverance","hope"]),
    ("Hebrews 10:23", "Let us hold fast the profession of our faith without wavering; for he is faithful that promised.", ["hope","faith","perseverance"]),
    ("James 1:12", "Blessed is the man that endureth temptation: for when he is tried, he shall receive the crown of life.", ["hardship","perseverance","motivation"]),
    ("Isaiah 40:31", "But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles.", ["tired","strength","hope","patience"]),
    ("Lamentations 3:22", "It is of the LORD'S mercies that we are not consumed, because his compassions fail not.", ["hope","hardship","mercy"]),
    ("Lamentations 3:23", "They are new every morning: great is thy faithfulness.", ["hope","new beginnings","faith"]),
    ("Psalm 31:24", "Be of good courage, and he shall strengthen your heart, all ye that hope in the LORD.", ["hope","courage","strength"]),
    ("Psalm 42:5", "Why art thou cast down, O my soul? and why art thou disquieted in me? hope thou in God.", ["hope","sadness","encouragement"]),
    ("Psalm 71:5", "For thou art my hope, O Lord GOD: thou art my trust from my youth.", ["hope","trust","faith"]),
    ("Psalm 130:5", "I wait for the LORD, my soul doth wait, and in his word do I hope.", ["hope","patience","trust"]),
    ("Micah 7:7", "Therefore I will look unto the LORD; I will wait for the God of my salvation: my God will hear me.", ["hope","patience","help"]),
    ("Zephaniah 3:17", "The LORD thy God in the midst of thee is mighty; he will save, he will rejoice over thee with joy.", ["hope","joy","courage"]),

    # Strength / motivation / work
    ("Philippians 4:13", "I can do all things through Christ which strengtheneth me.", ["strength","motivation","courage"]),
    ("1 Corinthians 15:58", "Therefore, my beloved brethren, be ye stedfast, unmoveable, always abounding in the work of the Lord.", ["motivation","perseverance","work"]),
    ("Colossians 3:23", "And whatsoever ye do, do it heartily, as to the Lord, and not unto men.", ["motivation","school","work"]),
    ("Proverbs 16:3", "Commit thy works unto the LORD, and thy thoughts shall be established.", ["work","future","trust","motivation"]),
    ("Proverbs 24:16", "For a just man falleth seven times, and riseth up again.", ["failure","motivation","perseverance"]),
    ("Ecclesiastes 9:10", "Whatsoever thy hand findeth to do, do it with thy might.", ["motivation","work","perseverance"]),
    ("Psalm 18:32", "It is God that girdeth me with strength, and maketh my way perfect.", ["strength","motivation","hope"]),
    ("Psalm 18:39", "For thou hast girded me with strength unto the battle: thou hast subdued under me those that rose up against me.", ["strength","courage","hardship"]),
    ("Psalm 28:7", "The LORD is my strength and my shield; my heart trusted in him, and I am helped.", ["strength","trust","help"]),
    ("Psalm 138:3", "In the day when I cried thou answeredst me, and strengthenedst me with strength in my soul.", ["strength","help","sadness"]),
    ("Isaiah 41:13", "For I the LORD thy God will hold thy right hand, saying unto thee, Fear not; I will help thee.", ["strength","fear","help"]),
    ("Ephesians 6:10", "Finally, my brethren, be strong in the Lord, and in the power of his might.", ["strength","courage","motivation"]),
    ("2 Thessalonians 3:13", "But ye, brethren, be not weary in well doing.", ["tired","motivation","perseverance"]),
    ("Hebrews 12:1", "Let us run with patience the race that is set before us.", ["motivation","patience","perseverance"]),
    ("1 Corinthians 16:13", "Watch ye, stand fast in the faith, quit you like men, be strong.", ["strength","courage","faith"]),

    # Wisdom / decisions / uncertainty
    ("Proverbs 3:5", "Trust in the LORD with all thine heart; and lean not unto thine own understanding.", ["trust","decisions","uncertainty"]),
    ("Proverbs 3:6", "In all thy ways acknowledge him, and he shall direct thy paths.", ["decisions","future","guidance"]),
    ("James 1:5", "If any of you lack wisdom, let him ask of God, that giveth to all men liberally.", ["wisdom","decisions","guidance"]),
    ("Psalm 32:8", "I will instruct thee and teach thee in the way which thou shalt go: I will guide thee with mine eye.", ["wisdom","guidance","future"]),
    ("Psalm 119:105", "Thy word is a lamp unto my feet, and a light unto my path.", ["wisdom","guidance","future"]),
    ("Proverbs 4:23", "Keep thy heart with all diligence; for out of it are the issues of life.", ["wisdom","decisions"]),
    ("Proverbs 16:9", "A man's heart deviseth his way: but the LORD directeth his steps.", ["decisions","future","guidance"]),
    ("Proverbs 19:21", "There are many devices in a man's heart; nevertheless the counsel of the LORD, that shall stand.", ["decisions","future","trust"]),
    ("Psalm 25:4", "Shew me thy ways, O LORD; teach me thy paths.", ["guidance","wisdom","decisions"]),
    ("Psalm 25:5", "Lead me in thy truth, and teach me: for thou art the God of my salvation.", ["guidance","wisdom","trust"]),
    ("Psalm 37:5", "Commit thy way unto the LORD; trust also in him; and he shall bring it to pass.", ["future","trust","decisions"]),
    ("Psalm 143:10", "Teach me to do thy will; for thou art my God: thy spirit is good; lead me into the land of uprightness.", ["guidance","decisions","wisdom"]),
    ("Colossians 3:16", "Let the word of Christ dwell in you richly in all wisdom.", ["wisdom","learning","guidance"]),
    ("Ephesians 5:15", "See then that ye walk circumspectly, not as fools, but as wise.", ["wisdom","decisions"]),
    ("Proverbs 2:6", "For the LORD giveth wisdom: out of his mouth cometh knowledge and understanding.", ["wisdom","learning","guidance"]),

    # Gratitude / joy / happiness
    ("Psalm 118:24", "This is the day which the LORD hath made; we will rejoice and be glad in it.", ["gratitude","joy","happiness"]),
    ("1 Thessalonians 5:18", "In every thing give thanks: for this is the will of God in Christ Jesus concerning you.", ["gratitude","joy","faith"]),
    ("Philippians 4:4", "Rejoice in the Lord alway: and again I say, Rejoice.", ["joy","happiness","gratitude"]),
    ("Psalm 100:4", "Enter into his gates with thanksgiving, and into his courts with praise: be thankful unto him.", ["gratitude","joy","worship"]),
    ("Psalm 107:1", "O give thanks unto the LORD, for he is good: for his mercy endureth for ever.", ["gratitude","hope","joy"]),
    ("Psalm 136:1", "O give thanks unto the LORD; for he is good: for his mercy endureth for ever.", ["gratitude","joy","hope"]),
    ("Nehemiah 8:10", "The joy of the LORD is your strength.", ["joy","strength","happiness"]),
    ("Psalm 16:11", "Thou wilt shew me the path of life: in thy presence is fulness of joy.", ["joy","hope","happiness"]),
    ("Psalm 30:11", "Thou hast turned for me my mourning into dancing.", ["joy","sadness","hope"]),
    ("Psalm 126:5", "They that sow in tears shall reap in joy.", ["sadness","joy","hope"]),
    ("Psalm 126:6", "He that goeth forth and weepeth, bearing precious seed, shall doubtless come again with rejoicing.", ["sadness","joy","hope"]),
    ("John 15:11", "These things have I spoken unto you, that my joy might remain in you, and that your joy might be full.", ["joy","happiness","hope"]),
    ("John 16:22", "Your heart shall rejoice, and your joy no man taketh from you.", ["joy","hope","happiness"]),
    ("Romans 12:15", "Rejoice with them that do rejoice, and weep with them that weep.", ["friendship","joy","sadness","compassion"]),
    ("Psalm 95:1", "O come, let us sing unto the LORD: let us make a joyful noise to the rock of our salvation.", ["joy","gratitude","worship"]),

    # Love / friendship / kindness / forgiveness
    ("1 Corinthians 13:4", "Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up.", ["love","kindness","friendship"]),
    ("1 Corinthians 13:7", "Beareth all things, believeth all things, hopeth all things, endureth all things.", ["love","hope","perseverance"]),
    ("1 Corinthians 13:13", "And now abideth faith, hope, charity, these three; but the greatest of these is charity.", ["love","faith","hope"]),
    ("John 15:12", "This is my commandment, That ye love one another, as I have loved you.", ["love","friendship","kindness"]),
    ("John 15:13", "Greater love hath no man than this, that a man lay down his life for his friends.", ["love","friendship"]),
    ("Proverbs 17:17", "A friend loveth at all times, and a brother is born for adversity.", ["friendship","love","hardship"]),
    ("Proverbs 18:24", "A man that hath friends must shew himself friendly: and there is a friend that sticketh closer than a brother.", ["friendship","love"]),
    ("Proverbs 27:17", "Iron sharpeneth iron; so a man sharpeneth the countenance of his friend.", ["friendship","motivation"]),
    ("Ecclesiastes 4:9", "Two are better than one; because they have a good reward for their labour.", ["friendship","relationships","help"]),
    ("Ecclesiastes 4:10", "For if they fall, the one will lift up his fellow.", ["friendship","help","hardship"]),
    ("Ephesians 4:32", "And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.", ["kindness","forgiveness","friendship"]),
    ("Colossians 3:13", "Forbearing one another, and forgiving one another, if any man have a quarrel against any.", ["forgiveness","conflict","friendship"]),
    ("Matthew 5:44", "Love your enemies, bless them that curse you, do good to them that hate you.", ["love","conflict","forgiveness"]),
    ("Luke 6:31", "And as ye would that men should do to you, do ye also to them likewise.", ["kindness","friendship","relationships"]),
    ("Micah 6:8", "He hath shewed thee, O man, what is good; and what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?", ["kindness","wisdom","faith"]),
    ("Proverbs 15:1", "A soft answer turneth away wrath: but grievous words stir up anger.", ["anger","conflict","kindness"]),
    ("Proverbs 12:18", "There is that speaketh like the piercings of a sword: but the tongue of the wise is health.", ["conflict","kindness","wisdom"]),

    # Faith / prayer / God's presence
    ("Psalm 121:1", "I will lift up mine eyes unto the hills, from whence cometh my help.", ["help","hope","faith"]),
    ("Psalm 121:2", "My help cometh from the LORD, which made heaven and earth.", ["help","faith","hope"]),
    ("Psalm 145:18", "The LORD is nigh unto all them that call upon him, to all that call upon him in truth.", ["prayer","help","faith"]),
    ("Jeremiah 33:3", "Call unto me, and I will answer thee, and shew thee great and mighty things.", ["prayer","help","guidance"]),
    ("Matthew 7:7", "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you.", ["prayer","hope","guidance"]),
    ("Matthew 7:8", "For every one that asketh receiveth; and he that seeketh findeth.", ["prayer","hope","faith"]),
    ("Psalm 18:2", "The LORD is my rock, and my fortress, and my deliverer; my God, my strength.", ["faith","strength","protection"]),
    ("Psalm 63:1", "O God, thou art my God; early will I seek thee: my soul thirsteth for thee.", ["faith","prayer","hope"]),
    ("Psalm 84:11", "For the LORD God is a sun and shield: the LORD will give grace and glory.", ["faith","hope","protection"]),
    ("Psalm 145:9", "The LORD is good to all: and his tender mercies are over all his works.", ["faith","hope","kindness"]),
    ("Hebrews 11:1", "Now faith is the substance of things hoped for, the evidence of things not seen.", ["faith","hope","uncertainty"]),
    ("Hebrews 11:6", "But without faith it is impossible to please him: for he that cometh to God must believe that he is.", ["faith","trust"]),
    ("Romans 10:17", "So then faith cometh by hearing, and hearing by the word of God.", ["faith","learning"]),
    ("Psalm 119:11", "Thy word have I hid in mine heart, that I might not sin against thee.", ["faith","wisdom"]),
    ("Psalm 119:114", "Thou art my hiding place and my shield: I hope in thy word.", ["faith","hope","protection"]),

    # Patience / waiting / new beginnings
    ("Psalm 37:7", "Rest in the LORD, and wait patiently for him.", ["patience","peace","future"]),
    ("Psalm 40:1", "I waited patiently for the LORD; and he inclined unto me, and heard my cry.", ["patience","hope","help"]),
    ("Ecclesiastes 3:1", "To every thing there is a season, and a time to every purpose under the heaven.", ["patience","future","change"]),
    ("Ecclesiastes 3:11", "He hath made every thing beautiful in his time.", ["patience","future","hope"]),
    ("Isaiah 43:19", "Behold, I will do a new thing; now it shall spring forth.", ["change","hope","new beginnings"]),
    ("2 Corinthians 5:17", "Therefore if any man be in Christ, he is a new creature: old things are passed away.", ["change","new beginnings","hope"]),
    ("Philippians 3:13", "Forgetting those things which are behind, and reaching forth unto those things which are before.", ["change","future","motivation"]),
    ("Psalm 30:5", "Weeping may endure for a night, but joy cometh in the morning.", ["patience","sadness","hope"]),
    ("James 5:7", "Be patient therefore, brethren, unto the coming of the Lord.", ["patience","hope","faith"]),
    ("Romans 5:3", "Tribulation worketh patience.", ["hardship","patience","perseverance"]),
    ("Romans 5:4", "And patience, experience; and experience, hope.", ["patience","hope","hardship"]),
    ("Romans 5:5", "And hope maketh not ashamed; because the love of God is shed abroad in our hearts.", ["hope","love","patience"]),
]

# More than 100 passages are intentionally included.
assert len(VERSES) >= 100

KEYWORDS = {
    "anxiety": ["anxious","anxiety","nervous","panic","worried","worry","overthinking","stress"],
    "fear": ["afraid","scared","fear","frightened","terrified"],
    "sadness": ["sad","down","cry","crying","unhappy","miserable","depressed"],
    "loneliness": ["lonely","alone","isolated","nobody","no one"],
    "hurt": ["hurt","broken","heartbroken","pain","betrayed"],
    "loss": ["lost","loss","grief","miss","death"],
    "anger": ["angry","mad","furious","annoyed","rage","upset"],
    "friendship": ["friend","friends","friendship","best friend"],
    "conflict": ["argument","fight","conflict","argued","fighting"],
    "forgiveness": ["forgive","forgiveness","guilt","mistake"],
    "gratitude": ["grateful","thankful","thank","blessed","appreciate"],
    "happiness": ["happy","great","amazing","awesome","excited"],
    "joy": ["joy","joyful","celebrate","celebration"],
    "motivation": ["motivation","motivated","give up","quit","hard","keep going"],
    "failure": ["failed","failure","mistake","messed up"],
    "school": ["school","homework","test","exam","grade","teacher"],
    "future": ["future","tomorrow","career","next year"],
    "decisions": ["decision","decide","choice","choose","should i"],
    "confusion": ["confused","confusing","don't know","unsure"],
    "trust": ["trust","faith","believe"],
    "peace": ["peace","calm","rest","relaxed"],
    "tired": ["tired","exhausted","weary","drained"],
    "overwhelmed": ["overwhelmed","too much","burden"],
    "strength": ["strong","strength","weak","courage"],
    "hope": ["hope","hopeless","better"],
    "love": ["love","loving","relationship"],
    "kindness": ["kind","kindness","compassion"],
    "wisdom": ["wisdom","advice","guidance"],
    "help": ["help","struggling","need help"],
    "patience": ["patient","waiting","wait","slow"],
    "change": ["change","new","moving","move","starting over"],
    "prayer": ["pray","prayer","praying"],
}

def detect_themes(text):
    lower = text.lower()
    scores = {}
    for theme, words in KEYWORDS.items():
        score = sum(1 for word in words if word in lower)
        if score:
            scores[theme] = score
    return sorted(scores, key=scores.get, reverse=True)

def choose_verse(text, avoid_ref=None):
    themes = detect_themes(text)
    if not themes:
        pool = [v for v in VERSES if v[0] != avoid_ref] or VERSES
        return random.choice(pool), ["general encouragement"]

    scored = []
    for verse in VERSES:
        score = sum(1 for theme in themes if theme in verse[2])
        if verse[0] == avoid_ref:
            score -= 2
        scored.append((score, random.random(), verse))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    best = scored[0][0]
    candidates = [v for s, _, v in scored if s == best]
    return random.choice(candidates[:8]), themes[:3]

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(105,85,175,.20), transparent 34%),
        linear-gradient(180deg,#090812,#12101b);
    color:#f7f4ff;
}
.block-container{max-width:780px;padding-top:3rem;padding-bottom:3rem}
.hero{text-align:center;padding:1.2rem 0}
.cross{font-size:46px}
h1{font-size:46px!important;letter-spacing:-.04em}
.subtitle{color:#aaa4b7}
.verse-card{
    background:linear-gradient(145deg,rgba(45,37,65,.97),rgba(22,20,31,.97));
    border:1px solid rgba(255,255,255,.10);
    border-radius:22px;padding:30px;margin:20px 0;
    box-shadow:0 20px 60px rgba(0,0,0,.3)
}
.verse-text{font-family:Georgia,serif;font-size:23px;line-height:1.7}
.verse-ref{margin-top:18px;color:#c6a9ff;font-weight:800}
.match-note{margin-top:12px;color:#aaa4b7;font-size:14px}
.stButton button{border-radius:12px;font-weight:800}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="cross">✝️</div>
<h1>VerseMatch</h1>
<p class="subtitle">Write what you're going through. Find a Bible verse that speaks to it.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### What's on your mind?")

text = st.text_area(
    "Write about your day, your feelings, something that happened, or a question you have.",
    placeholder="For example: I'm nervous about tomorrow and I keep worrying that I won't be good enough...",
    height=180,
    label_visibility="collapsed",
)

c1, c2 = st.columns([2,1])
with c1:
    find = st.button("✦ Find my verse", use_container_width=True, type="primary")
with c2:
    clear = st.button("Clear", use_container_width=True)

if clear:
    st.session_state.pop("verse_result", None)
    st.rerun()

if find:
    if not text.strip():
        st.warning("Write a little about what you're experiencing first.")
    else:
        st.session_state.verse_result = choose_verse(text)

if "verse_result" in st.session_state:
    verse, themes = st.session_state.verse_result
    ref, quote, verse_themes = verse
    theme_text = ", ".join(themes)

    st.markdown(
        f"""
        <div class="verse-card">
            <div class="verse-text">“{quote}”</div>
            <div class="verse-ref">{ref}</div>
            <div class="match-note">
                Matched around themes of {theme_text}.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "This is a theme-based suggestion and does not claim to know exactly how you feel."
    )

    if st.button("↻ Show another fitting verse", use_container_width=True):
        st.session_state.verse_result = choose_verse(text, avoid_ref=ref)
        st.rerun()

st.markdown("---")
st.caption(f"VerseMatch contains {len(VERSES)} Bible passages. The included wording is from the public-domain King James Version.")

