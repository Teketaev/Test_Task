1. В терминал - git clone https://github.com/Teketaev/Test_Task.git
2. В терминал - cd Test_Task/payments
3. Создайте .env файл в project root(в папке Test_Task)
4. (Тут вводятся ваши данные из https://dashboard.stripe.com/test/apikeys) Вставьте в .env(Каждое значение на отдельной линии) - STRIPE_PUBLIC_KEY='вставьте свой Public Key из Stripe'
STRIPE_SECRET_KEY='вставьте свой Secret Key из Stripe'
6. В терминал - docker-compose build
7. В терминал - docker-compose up -d
8. Перейдите в http://localhost:8000/ на своем браузере

Заметка: Если при нажатии [Buy] и [Proceed to Checkout] ничего не происходит также замените в payments/base/templates/base/item.html и order.html - var stripe = Stripe('Вставьте сюда свой Public Key');
