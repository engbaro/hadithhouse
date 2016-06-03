from django.test import TestCase
from django.test.testcases import SimpleTestCase

from textprocessing.arabic import remove_arabic_diacritics, unify_alef_letters, simplify_arabic_text
from textprocessing.generic import multiline_to_singleline, remove_brackets_whitespaces, reformat_text
from textprocessing.regex import DocScanner


class GenericTestCase(SimpleTestCase):
  def test_multiline_to_singleline(self):
    input = 'My name is \n  Rafid \r Khalid'
    output = multiline_to_singleline(input)
    self.assertEqual('My name is Rafid Khalid', output)

  def test_remove_brackets_whitespaces(self):
    input = 'This is a text with (  incorrect whitespaces between brackets   ).'
    output = remove_brackets_whitespaces(input)
    self.assertEqual('This is a text with (incorrect whitespaces between brackets).', output)

  def test_reformat_text(self):
    input = u'''
   أَخْبَرَنَا أَبُو جَعْفَرٍ مُحَمَّدُ بْنُ يَعْقُوبَ قَالَ حَدَّثَنِي عِدَّةٌ مِنْ أَصْحَابِنَا مِنْهُمْ مُحَمَّدُ بْنُ
يَحْيَى الْعَطَّارُ عَنْ أَحْمَدَ بْنِ مُحَمَّدٍ عَنِ الْحَسَنِ بْنِ مَحْبُوبٍ عَنِ الْعَلَاءِ بْنِ رَزِينٍ عَنْ مُحَمَّدِ بْنِ مُسْلِمٍ
عَنْ أَبِي جَعْفَرٍ ( عليه السلام )قَالَ لَمَّا خَلَقَ اللَّهُ الْعَقْلَ اسْتَنْطَقَهُ ثُمَّ قَالَ لَهُ أَقْبِلْ فَأَقْبَلَ ثُمَّ قَالَ لَهُ أَدْبِرْ
فَأَدْبَرَ ثُمَّ قَالَ وَ عِزَّتِي وَ جَلَالِي مَا خَلَقْتُ خَلْقاً هُوَ أَحَبُّ إِلَيَّ مِنْكَ وَ لَا أَكْمَلْتُكَ إِلَّا فِيمَنْ
أُحِبُّ أَمَا إِنِّي إِيَّاكَ آمُرُ وَ إِيَّاكَ أَنْهَى وَ إِيَّاكَ أُعَاقِبُ وَ إِيَّاكَ أُثِيبُ .
    '''
    output = reformat_text(input)
    expected = u'''
أَخْبَرَنَا أَبُو جَعْفَرٍ مُحَمَّدُ بْنُ يَعْقُوبَ قَالَ حَدَّثَنِي عِدَّةٌ مِنْ أَصْحَابِنَا مِنْهُمْ مُحَمَّدُ بْنُ يَحْيَى الْعَطَّارُ عَنْ أَحْمَدَ بْنِ مُحَمَّدٍ عَنِ الْحَسَنِ بْنِ مَحْبُوبٍ عَنِ الْعَلَاءِ بْنِ رَزِينٍ عَنْ مُحَمَّدِ بْنِ مُسْلِمٍ عَنْ أَبِي جَعْفَرٍ (عليه السلام)قَالَ لَمَّا خَلَقَ اللَّهُ الْعَقْلَ اسْتَنْطَقَهُ ثُمَّ قَالَ لَهُ أَقْبِلْ فَأَقْبَلَ ثُمَّ قَالَ لَهُ أَدْبِرْ فَأَدْبَرَ ثُمَّ قَالَ وَ عِزَّتِي وَ جَلَالِي مَا خَلَقْتُ خَلْقاً هُوَ أَحَبُّ إِلَيَّ مِنْكَ وَ لَا أَكْمَلْتُكَ إِلَّا فِيمَنْ أُحِبُّ أَمَا إِنِّي إِيَّاكَ آمُرُ وَ إِيَّاكَ أَنْهَى وَ إِيَّاكَ أُعَاقِبُ وَ إِيَّاكَ أُثِيبُ .
    '''.strip()
    self.assertEqual(expected, output)


class ArabicTestCase(SimpleTestCase):
  def test_remove_arabic_diacritic(self):
    input = 'اخْتِبار ازَاْلة عَلامات التَشْكيل'
    output = remove_arabic_diacritics(input)
    self.assertEqual('اختبار ازالة علامات التشكيل', output)

  def test_unify_alef_letters(self):
    input = 'اآأإٱٲٳٵ'
    output = unify_alef_letters(input)
    self.assertEqual('اااااااا', output)

  def test_simplify_arabic_text_for_surat_alfatiha(self):
    self.assertEqual('بسم الله الرحمن الرحيم', simplify_arabic_text('بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'))
    self.assertEqual('الحمد لله رب العالمين', simplify_arabic_text('الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ'))
    self.assertEqual('الرحمن الرحيم', simplify_arabic_text('الرَّحْمَنِ الرَّحِيمِ'))
    self.assertEqual('مالك يوم الدين', simplify_arabic_text('مَالِكِ يَوْمِ الدِّينِ'))
    self.assertEqual('اياك نعبد واياك نستعين', simplify_arabic_text('إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ'))
    self.assertEqual('اهدنا الصراط المستقيم', simplify_arabic_text('اهدِنَا الصِّرَاطَ الْمُسْتَقِيمَ'))
    self.assertEqual('صراط الذين انعمت عليهم غير المغضوب عليهم ولا الضالين', simplify_arabic_text(
      'صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلاَ الضَّالِّينَ'))

  def test_simplify_arabic_text_for_different_alef_types(self):
    # TODO: Add tests for the rest of Alef types.
    self.assertEqual('امنا', simplify_arabic_text('آمَنَّا'))
    self.assertEqual('اولئك', simplify_arabic_text('أُوْلَئِكَ'))
    self.assertEqual('او', simplify_arabic_text('أَوْ'))
    self.assertEqual('واذا', simplify_arabic_text('وَإِذَا'))
    pass


class DocumentScannerTestCase(SimpleTestCase):
  def test_scan_bullet_points(self):
    numbers_found = []

    def found_number(type, prev_type, match, prev_match, document):
      self.assertEqual('number', type)
      self.assertIsNotNone(match.group('number_value'))
      numbers_found.append(match.group('number_value'))

    document = '1. First bullet point 2. Second bullet point'

    ds = DocScanner({
      'number': r'(?P<number_value>[0-9]+)\.'
    }, found_number)
    ds.scan(document)

    self.assertEqual(['1', '2'], numbers_found)

  def test_scan_simple_book(self):
    book = '''
Chapter 1: Title of Chapter 1
Section 1.1: Title of Section 1 of Chapter 1
Section 1.2: Title of Section 2 of Chapter 1
Chapter 2: Title of Chapter 2
Section 2.1: Title of Section 1 of Chapter 2
Section 2.2: Title of Section 2 of Chapter 2
    '''

    tokens_found = []

    def found_token(type, prev_type, match, prev_match, document):
      self.assertIn(type, ['chapter', 'section'])

      if type == 'chapter':
        self.assertIsNotNone(match.group('chapter_number'))
        self.assertIsNotNone(match.group('chapter_title'))
        tokens_found.append({
          'number': match.group('chapter_number'),
          'title': match.group('chapter_title'),
        })
      elif type == 'section':
        self.assertIsNotNone(match.group('section_number'))
        self.assertIsNotNone(match.group('section_title'))
        tokens_found.append({
          'number': match.group('section_number'),
          'title': match.group('section_title'),
        })
      else:
        self.fail()

    ds = DocScanner({
      'chapter': r'^Chapter (?P<chapter_number>[0-9]+): (?P<chapter_title>.*)$',
      'section': r'^Section (?P<section_number>[0-9]+\.[0-9]+): (?P<section_title>.*)$',
    }, found_token)
    ds.scan(book)

    self.assertListEqual([
      {'number': '1', 'title': 'Title of Chapter 1'},
      {'number': '1.1', 'title': 'Title of Section 1 of Chapter 1'},
      {'number': '1.2', 'title': 'Title of Section 2 of Chapter 1'},
      {'number': '2', 'title': 'Title of Chapter 2'},
      {'number': '2.1', 'title': 'Title of Section 1 of Chapter 2'},
      {'number': '2.2', 'title': 'Title of Section 2 of Chapter 2'},
    ], tokens_found)
