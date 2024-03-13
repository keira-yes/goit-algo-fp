### Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

-   написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
-   розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
-   написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

### Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

### Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

### Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
![Бінарна купа](heap.png)

### Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

### Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

### Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

| Сума | Імовірність   |
| ---- | ------------- |
| 2    | 2.78% (1/36)  |
| 3    | 5.56% (2/36)  |
| 4    | 8.33% (3/36)  |
| 5    | 11.11% (4/36) |
| 6    | 13.89% (5/36) |
| 7    | 16.67% (6/36) |
| 8    | 13.89% (5/36) |
| 9    | 11.11% (4/36) |
| 10   | 8.33% (3/36)  |
| 11   | 5.56% (2/36)  |
| 12   | 2.78% (1/36)  |

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

### Висновки щодо методу Монте-Карло

Метод Монте-Карло був використаний для моделювання кидків двох ігрових кубиків з метою обчислення ймовірностей випадіння кожної можливої суми чисел. Симуляція включала 100,000 кидків, на основі яких були обчислені ймовірності сум від 2 до 12.

Моделювання методом Монте-Карло показало наступні ймовірності:

![Монте Карло](monte_carlo.png)

| Сума | Імовірність |
| ---- | ----------- |
| 2    | 2.82%       |
| 3    | 5.60%       |
| 4    | 8.15%       |
| 5    | 10.94%      |
| 6    | 14.06%      |
| 7    | 16.74%      |
| 8    | 13.87%      |
| 9    | 11.02%      |
| 10   | 8.41%       |
| 11   | 5.63%       |
| 12   | 2.77%       |

Результати, отримані за допомогою методу Монте-Карло, дуже близькі до аналітичних розрахунків. Це підтверджує точність і надійність методу Монте-Карло для обчислення ймовірностей у подібних статистичних задачах. Найбільша ймовірність обох методів припадає на суму 7, що відповідає теоретичному розрахунку, враховуючи кількість комбінацій, які дають цю суму.

Метод Монте-Карло ефективний для вирішення задач, де аналітичне розв'язання є складним або неможливим. Він дозволяє отримати точні оцінки з допомогою великої кількості ітерацій експерименту, що робить його корисним інструментом у області статистики та ймовірності.
