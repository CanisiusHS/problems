import check50
import check50.py


@check50.check()
def exists():
    """readability.py exists"""
    check50.exists("readability.py")


@check50.check(exists)
def compiles():
    """readability.py is valid Python"""
    check50.py.compile("readability.py")


@check50.check(compiles)
def single_sentence():
    """handles a single sentence with multiple words"""
    text = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 7\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def single_sentence_other_punctuation():
    """handles punctuation within a single sentence"""
    text = "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 9\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def multiple_sentences():
    """handles multiple sentences"""
    text = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 5\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def multiple_sentences_complex():
    """handles multiple, more complex sentences"""
    text = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 10\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def longer_passage():
    """handles a longer multi-sentence passage"""
    text = "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 8\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def exclamation_marks():
    """handles sentences ending in exclamation marks"""
    text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
    check50.run("python3 readability.py").stdin(text).stdout("Grade 3\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def question_marks():
    """handles sentences ending in question marks"""
    text = "Would you like them here or there? I would not like them here or there. I would not like them anywhere."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 2\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def before_grade_1():
    """handles text below Grade 1"""
    text = "One fish. Two fish. Red fish. Blue fish."
    check50.run("python3 readability.py").stdin(text).stdout("Before Grade 1\n").stdout(check50.EOF).exit(0)


@check50.check(compiles)
def grade_16_plus():
    """handles text at Grade 16+ (note: literal '+' character, not regex)"""
    text = "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."
    check50.run("python3 readability.py").stdin(text).stdout("Grade 16+\n", regex=False).stdout(check50.EOF).exit(0)
