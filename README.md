# MMDS Final Project Task

![Task](task.jpg)

--- 

# Plan

1. <span style="color:green">Yura: </span>використовуючи 20% семплінг, скачати 40к+ едітів з стріму вікі, але не юзаючи юзернейм для семплінгу (треба подумати які філди використати для цього)
2. <span style="color:green">Yura: </span>показати дістріб'юшени даних (скіко людей/ботів)
3. <span style="color:yellow">Denys: </span>натренувати якийсь класифікатор, наприклад рандом форест, (використовуючи ці 40к+ едітів)
4. <span style="color:yellow">Tetiana: </span>імплементувати блум фільтр, підібрати параметри так, щоб пробабіліті помилки був близько 10%
5. <span style="color:green">Yura: </span>закинути то все в докер щоб працювало зі спарк стрімінгом в режимі реального часу (інферес модельки та блум фільтр)

--- 

# Docker startup
1. From inside the /mmds folder run `docker build -t mmds .`
2. Run using `docker run --rm -p 9999:9999 mmds`