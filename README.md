# brusnika
тестовое для брусники

Для запуска приложения необходимо запустить 'run.sh' командой ```sh run.sh```.

Страницы приложения:
- /api/menu_items — страница API меню. Методом GET можем получить всё меню, методом POST добавить новый элемент.
- /app/list — страница с пунктами меню, рассортированными по категориям. На плюсик выполняется добавление пункта меню в заказ.
- /app/bill — страница счёта меню. Здесь выводится сумма заказа, список выбранных блюд и список алергенов (пока не сделал).