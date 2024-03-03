1. В терминал - git clone https://github.com/Teketaev/Test_Task.git
2. В терминал - cd Test_Task/payments
3. Создайте .env файл в project root(в папке Test_Task)
4. (Тут вводятся ваши данные из https://dashboard.stripe.com/test/apikeys) Вставьте в .env - STRIPE_PUBLIC_KEY=<вставьте свой Public Key из Stripe>, STRIPE_SECRET_KEY=<вставьте свой Secret Key из Stripe>
5. В терминал - docker-compose build
6. В терминал - docker-compose up -d
7. Перейдите в http://localhost:8000/ на своем браузере
