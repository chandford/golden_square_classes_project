from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
When we add (a) Diary Entry/Entries
It is/they are saved to the Diary
"""
def test_diary_add_adds_diaryentry_instances():
    entry = DiaryEntry("My Title", "diary contents")
    diary = Diary()
    assert diary.entry_list == []
    diary.add(entry)
    diary.add(entry) 
    assert len(diary.entry_list) == 2
    assert isinstance(diary.entry_list[1], DiaryEntry)

"""
When we add multiple Diary Entries
They are saved to the Diary
And are listed with "all"
"""
def test_all_returns_all_diaryentry_instances():
    entry_1 = DiaryEntry("My Title", "diary contents")
    entry_2 = DiaryEntry("New Title", "extra diary contents")
    entry_3 = DiaryEntry("Bonus Title", "final diary contents")

    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2) 
    diary.add(entry_3) 
    assert len(diary.all()) == 3
    first_entry = diary.all()[1]
    assert first_entry.title == "New Title"


"""
When we add multiple Diary Entries
And we run count_words
We get the sum of all entries contained in the Diary
"""
def test_count_words_totals_all_entries_word_count():
    entry_1 = DiaryEntry("My Title", "diary contents")
    entry_2 = DiaryEntry("New Title", "extra diary contents")
    entry_3 = DiaryEntry("Bonus Title", "final diary contents")

    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2) 
    assert diary.count_words() == 5
    diary.add(entry_3) 
    assert diary.count_words() == 8


"""
When we add multiple Diary Entries
And we run reading_time
We get an estimate of the reading time for all entries back
"""
def test_reading_time_totals_all_entries_reading_time():
    entry_1 = DiaryEntry("My Title", "diary contents")
    entry_2 = DiaryEntry("New Title", "1 2 3 4 5 6 7 8 9 0")
    entry_3 = DiaryEntry("Third Title", "1 2 3 4 5 6 7 8 9 0")

    diary = Diary()
    diary.add(entry_1)
    assert diary.reading_time(1) == 2 # 2 words to read
    diary.add(entry_2)
    assert diary.reading_time(2) == 6 # 12 words to read
    diary.add(entry_3) 
    assert diary.reading_time(4) == 5 # 22 words to read

"""
When we add multiple Diary Entries
And we search for a word not in any track title
We get an empty list back
"""
def test_find_best_entry_returns_closest_matching_diary_entry():
    entry_1 = DiaryEntry("My Title", "diary contents")
    entry_2 = DiaryEntry("New Title", "1 2 3 4")
    entry_3 = DiaryEntry("Third Title", "1 2 3 4 5 6 7 8 9 0")

    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3) 
    assert isinstance(diary.find_best_entry_for_reading_time(2, 2), DiaryEntry)
    chosen_entry = diary.find_best_entry_for_reading_time(2, 2)
    assert chosen_entry.title == "New Title"
    chosen_entry = diary.find_best_entry_for_reading_time(10, 20)
    assert chosen_entry.title == "Third Title"



