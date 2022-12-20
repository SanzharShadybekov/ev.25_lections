# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100

# SELECT * FROM work WHERE source='Moby' AND totalparagraphs < 100;

# 2. Найти кол-во глав в каждом произведении
# SELECT COUNT(*), work.title FROM chapter JOIN work
# ON work.workid = chapter.workid
# GROUP BY work.title ORDER BY count(*) DESC;
