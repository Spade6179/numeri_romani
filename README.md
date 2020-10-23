# numeri_romani.py
*Converting Roman Numerals (Latin: **numeri romani**) in Python, using TDD with Hypothesis*

After watching Robert "Uncle Bob" Martin's [seminars](https://youtu.be/7EmboKQH8lM) and Scott Lwaschin's NDC [talk](https://youtu.be/IYzDFHx6QPY), I was inspired to practice more Test-Driven Design in my code. [Hypothesis](https://hypothesis.readthedocs.io/) is the closest Python equivalent to Haskell's Quickcheck library, so I integrated it into my unit tests.

The most difficult part for me was testing that the numerals were in order without re-implementing the code itself. Lwaschin warns about this precise trap in his talk. I decided to mimic Martin's approach and finally had a dozen tests. His style reminds me a lot of Sherlock Holmes in that he narrows down BIG concepts into trivial edge tests that, one-by-one, leave few possibilities for error. Despite this, I still found erroneous output that wasn't caught by any of my tests.

I found that my resources (and understanding) of Roman Numerals was lacking, so I did more research. I found [this](https://juehan.github.io/DiveIntoPython3_Korean_Translation/unit-testing.html) tutorial by Mark Pilgrim specifically about this problem. It included this *beautiful* regular expression that made me shed tears of joy:

`^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$`

(I erroneously attributed the pattern to Juehan Lee in the code. [Too bad!](https://www.youtube.com/watch?v=k238XpMMn38))

This expression sets the syntactical guidelines for a valid string of numerals. It makes a few of the tests I wrote redundant, but I decided to keep them to make debugging easier. If I wanted to, I could probably expand Pilgrim's test to narrow down the issue piecemeal, but the setup works fine as-is.

Per Martin's recommendation, I also tried to reduce the number of comments I used and write clean variable names instead. I'm sure Martin would have something to say about the length of the final function, but I can't see how I can split it up any further with being pedantic or obtuse...

Feel free to share any recommendations on improvement!
