# Debug Review
### Nicolas Flandrois
### Thu 06 May 2021 11:22:04 CEST

##### Isue [efe/netflix - API resquest issues in User Athentication - No acccess to the page to scrap any data](https://github.com/efe/netflix/issues/2#issue-877260787)
##### Results of investigation in this issue

The error message:

```
/<usr/path-to-folder>/netflix/netflix/models.py", line 35, in fetch
metadata = json.loads(metadata_script_tag.string)
AttributeError: 'NoneType' object has no attribute 'string'
```

When I pushed my investigations further, it appears that your response object (netflix/models.py line 32) is automatically redirected from the API URL to Netflix Welcome page.

If you unfold your `soup = BeautifulSoup(response.content, "html.parser")` object (netflix/models.py line 33) in a :

```python
print(soup.text)
```
your outcome will look like:
```
Netflix - Watch TV Shows Online, Watch Movies OnlineNetflix and third parties use cookies and similar technologies on this website to collect information about your browsing activities which we use to analyse your use of the website, to personalize our services and to customise our online advertisements. Netflix supports the Digital Advertising Alliance Principles. Learn more about our use of cookies and information. By clicking accept, you accept the use of all cookies and your information for the purposes mentioned above.Netflix and third parties use cookies (why?). You can change (your cookie preferences); by clicking accept, you accept all cookies.AcceptChange your cookie preferencesCloseNetflixSign InUnlimited movies, TV shows, and more.Watch anywhere. Cancel anytime.Get StartedchevronEnjoy on your TV.Watch on Smart TVs, Playstation, Xbox, Chromecast, Apple TV, Blu-ray players, and more.Download your shows to watch offline.Save your favorites easily and always have something to watch.Stranger ThingsDownloading...Watch everywhere.Stream unlimited movies and TV shows on your phone, tablet, laptop, and TV without paying more.Create profiles for kids.Send kids on adventures with their favorite characters in a space made just for them—free with your membership.Frequently Asked QuestionsWhat is Netflix?Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, and more on thousands of internet-connected devices.You can watch as much as you want, whenever you want without a single commercial – all for one low monthly price. There's always something new to discover and new TV shows and movies are added every week!How much does Netflix cost?Watch Netflix on your smartphone, tablet, Smart TV, laptop, or streaming device, all for one fixed monthly fee. Plans range from EUR7.99 to EUR15.99 a month. No extra costs, no contracts.Where can I watch?Watch anywhere, anytime, on an unlimited number of devices. Sign in with your Netflix account to watch instantly on the web at netflix.com from your personal computer or on any internet-connected device that offers the Netflix app, including smart TVs, smartphones, tablets, streaming media players and game consoles.You can also download your favorite shows with the iOS, Android, or Windows 10 app. Use downloads to watch while you're on the go and without an internet connection. Take Netflix with you anywhere.How do I cancel?Netflix is flexible. There are no pesky contracts and no commitments. You can easily cancel your account online in two clicks. There are no cancellation fees – start or stop your account anytime.What can I watch on Netflix?Netflix has an extensive library of feature films, documentaries, TV shows, anime, award-winning Netflix originals, and more. Watch as much as you want, anytime you want.Is Netflix good for kids?The Netflix Kids experience is included in your membership to give parents control while kids enjoy family-friendly TV shows and movies in their own space.Kids profiles come with PIN-protected parental controls that let you restrict the maturity rating of content kids can watch and block specific titles you don’t want kids to see.Get StartedchevronQuestions? Call (+33) 0805-543-064FAQHelp CenterAccountMedia CenterInvestor RelationsJobsRedeem Gift CardsBuy Gift CardsWays to WatchTerms of UsePrivacyCookie PreferencesCorporate InformationContact UsSpeed TestLegal NoticesNetflix OriginalsSelect LanguageFrançaisEnglishNetflix France
```
Which text corresponds to the welcome page from Netflix, if not logged in.

I finally could test, with a Netflix account open in a web browser, the issue remains.
As your script/package doesn't use the same authenticated port as the web browser, the connexion isn't recognised. (kinda logic)

Apparently, you need to be authenticated, in order to access any data for your BeautifulSoup4 web scrapping.
I would recommend you to have a look to:
https://github.com/jameskang410/scraping-netflix
He handles authentication in his project.



---
# Original Readme Documentation:
---
# netflix

[![Build Status](https://travis-ci.org/efe/netflix.svg?branch=master)](https://travis-ci.org/efe/netflix) [![pypi](https://img.shields.io/pypi/v/netflix.svg)](https://pypi.org/project/netflix/)

A Python client for Netflix.

## Installation

```
pip install netflix
```

## Documentation

### Netflix ID

- **Movie**: The Intern
- **URL**: `https://www.netflix.com/watch/80047616`
- **Netflix ID**: `80047616`

### Movie

```python
from netflix import Movie

movie = Movie("80047616")
print(movie.name)  # 'The Intern'
```

#### Attributes

- `name`: `'The Intern'`
- `genre`: `'Comedies'`
- `description`: `'Harried fashion entrepreneur Jules gets a surprise boost from Ben, a 70-year-old widower who answers an ad seeking a senior intern.'`
- `image_url`: `'https://occ-0-2774-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABW8TwHJmfYqEjUj0YK4Y2ugq-sKIN-Gi8OBaDjOh3SbRSBdbEXlmpWEpHTbrO2CLDdo7yxRl7MTm5YtYa1-71Kg1o-7o.jpg?r=2ce'`
- `metadata`

### TVShow

```python
from netflix import TVShow

tv_show = TVShow("80192098")
print(tv_show.name)  # 'Money Heist'
```

#### Attributes

- `name`: `'Money Heist'`
- `genre`: `'TV Thrillers'`
- `description`: `'Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan.'`
- `image_url`: `'https://occ-0-2774-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABRQ7vD9Tg2GJUxLlWRw85C9Ln3j_m3dMvVhpf-LAJLDg9JNVsQKRyqvwlH28uoYY_gW7ROp1CI1PYdkBIlJwxpB8_VzK.jpg?r=8f1'`
- `metadata`

### Extra

#### Fetch Instantly

Default is `True`

```python
from netflix import Movie

movie = Movie("80047616", fetch_instantly=False)

# Do something.

movie.fetch()
```

#### Metadata

```python
from netflix import Movie

movie = Movie("80047616")

print(movie.metadata)
"""
{
  '@context': 'http://schema.org',
  '@type': 'Movie',
  'url': 'https://www.netflix.com/tr-en/title/80047616',
  'contentRating': '16+',
  'name': 'The Intern',
  'description': 'Harried fashion entrepreneur Jules gets a surprise boost from Ben, a 70-year-old widower who answers an ad seeking a senior intern.',
  'genre': 'Comedies',
  'image': 'https://occ-0-2773-2774.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABW8TwHJmfYqEjUj0YK4Y2ugq-sKIN-Gi8OBaDjOh3SbRSBdbEXlmpWEpHTbrO2CLDdo7yxRl7MTm5YtYa1-71Kg1o-7o.jpg?r=2ce',
  'dateCreated': '2019-8-31',
  'actors': [{
    '@type': 'Person',
    'name': 'Robert De Niro'
  }, {
    '@type': 'Person',
    'name': 'Anne Hathaway'
  }, {
    '@type': 'Person',
    'name': 'Rene Russo'
  }, {
    '@type': 'Person',
    'name': 'Anders Holm'
  }, {
    '@type': 'Person',
    'name': 'JoJo Kushner'
  }, {
    '@type': 'Person',
    'name': 'Andrew Rannells'
  }, {
    '@type': 'Person',
    'name': 'Adam Devine'
  }, {
    '@type': 'Person',
    'name': 'Zack Pearlman'
  }, {
    '@type': 'Person',
    'name': 'Jason Orley'
  }, {
    '@type': 'Person',
    'name': 'Christina Scherer'
  }],
  'creator': [],
  'director': [{
    '@type': 'Person',
    'name': 'Nancy Meyers'
  }]
}
"""
```
