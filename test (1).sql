-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Сен 09 2022 г., 22:32
-- Версия сервера: 5.6.51-log
-- Версия PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `test`
--

-- --------------------------------------------------------

--
-- Структура таблицы `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Торты'),
(2, 'Десерты'),
(3, 'Горячие напитки'),
(4, 'Холодные напитки\r\n');

-- --------------------------------------------------------

--
-- Структура таблицы `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `text` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `comments`
--

INSERT INTO `comments` (`id`, `username`, `text`) VALUES
(1, 'muhammadsaid_vosidov', 'ok'),
(2, 'muhammadsaid_vosidov', 'f'),
(3, 'muhammadsaid_vosidov', '/sart'),
(4, 'nazirjon_ismoiljonov', 'fd'),
(5, 'muhammadsaid_vosidov', '? назад'),
(6, 'muhammadsaid_vosidov', 'Yd'),
(7, 'muhammadsaid_vosidov', 'Test'),
(8, 'muhammadsaid_vosidov', '? назад'),
(9, 'muhammadsaid_vosidov', 'hk'),
(10, 'muhammadsaid_vosidov', 'rdtg'),
(11, 'abdu', 'зур'),
(12, 'username_telegram', 'зур'),
(13, 'nazirjon_ismoiljonov', 'dfgdf'),
(14, 'nazirjon_ismoiljonov', 'оки'),
(15, 'nazirjon_ismoiljonov', 'рахмат'),
(16, 'nazirjon_ismoiljonov', '? Начать заказывать'),
(17, 'muhammadsaid_vosidov', 'Салом'),
(18, 'nazirjon_ismoiljonov', 'Ок'),
(19, 'muhammadsaid_vosidov', 'heeeeellloooo'),
(20, 'muhammadsaid_vosidov', 'Hi bot');

-- --------------------------------------------------------

--
-- Структура таблицы `on_time`
--

CREATE TABLE `on_time` (
  `id` int(11) NOT NULL,
  `user_id` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `pipeline` int(11) NOT NULL,
  `language` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `product` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `on_time`
--

INSERT INTO `on_time` (`id`, `user_id`, `username`, `pipeline`, `language`, `product`, `price`, `amount`) VALUES
(1, '1883517936', 'muhammadsaid_vosidov', 1, 'config_taj', 'Белый трюфель', 100, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username_telegram` text NOT NULL,
  `username` text NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL,
  `products` text NOT NULL,
  `price` int(11) NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `user_id`, `username_telegram`, `username`, `phone`, `address`, `products`, `price`, `data`) VALUES
(136, 1883517936, 'muhammadsaid_vosidov', '-', '-', 'st. 279', 'Кофе РАФ - 6шт. x 20 = 120 сомони\n', 120, '2022-07-28 23.37.16'),
(137, 1883517936, 'muhammadsaid_vosidov', '-', '-', 'st. 279', 'Кофе РАФ - 6шт. x 20 = 120 сомони\nАфганка (наполеон) - 2шт. x 14 = 28 сомони\n', 148, '2022-07-29 00.02.51'),
(138, 1883517936, 'muhammadsaid_vosidov', 'G', 'st. 279', '+992400084277', 'Муссовый \'Белый бархат\' - 5шт. x 20 = 100 сомони\n', 100, '2022-08-22 22.24.10'),
(139, 1883517936, 'muhammadsaid_vosidov', 'G', 'st. 279', '+992400084277', 'Идеал - 6шт. x 80 = 480 сомони\n', 480, '2022-08-22 22.24.10');

-- --------------------------------------------------------

--
-- Структура таблицы `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `category` text NOT NULL,
  `name` text NOT NULL,
  `price` text NOT NULL,
  `photo` text NOT NULL,
  `description` text NOT NULL,
  `general_product` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `products`
--

INSERT INTO `products` (`id`, `category`, `name`, `price`, `photo`, `description`, `general_product`) VALUES
(1, 'Торты', 'Апельсин в шоколаде', '110', 'https://lh3.googleusercontent.com/-zvftd63tpRpuUjLBkGJUCl_DAkSWSXuFL8l8X30A3i0Ul45kLTW8BIKnCiqEh0JpB6NgRwTyIZ_5upluEEH30xeTNFd9hUFeIwQ4bAHhvAJaKV3QSCHL2t7Zdqs5y3JwLzDKIyNojYBaJFtIOFymFEXSDEMXaOgZ22UNbfnA1p0jJ_8LMZbRlQSN6c8OwkeLR4MG_WxiJuOLB63IH26PrxQv8Kj8npQKXIrpzdGuChR9oa6KYU9y8xUksdAsVSdUrqjgMwh-T23U2ITadK2f62Z5xEYs9uh8KeItP-4uLH2uMPJjjDXeeu_uTLPUz7_B67-fkDC-shzPaJ21PflEHF3OKaFIgkXJOoScjodieH7B7YIDj9YUajav7gfPTLudnZxzyd9jbHunLWFQGsK0x8zsT1jF34MCVX3IGN4ZztQWBy6Ad10b5EBze69EmWn-hAn9T3mf1a4PCRKvoLwiSFIlLTYJwv3mT43edHi2QiEDh1XTw4p6WJOx18WopQetToPD0H_OjBwl5iGgSY77XkMTp_x0fty8uVH9jG0GP0mJWaeoVnMwad8YM6dvkthB__RRFrcgNGposSfBzcGDHyAlPlrWFYUe5b6neNilElDlid89y5G74JfixWqtUSafQ41gH5kQKlS2qH_5QNTv6Rf0K5bsd3tesfvmyOTkx7MisOpmRP03lSC4MY-ZpzIf9qzW0OuzmZz8OQWTBM5WRFoZDsecOH85ZIsq3lYoHpNCMH5-S4OWdTXD009VifYiVCQw9h1cBaXpwEPsiZJudk9K8zSRqvl=w212-h238-no?authuser=0', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 2),
(3, 'Торты', 'Белый трюфель', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов\r\n', 0),
(4, 'Торты', 'Восторг ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(5, 'Торты', 'Идеал', '80', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(6, 'Торты', 'Капучино ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(7, 'Торты', 'Карамелька ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(8, 'Торты', 'Лимонный страсть ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(9, 'Торты', 'Малина в шоколаде ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(10, 'Торты', 'Марчелло', '120', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(11, 'Торты', 'Медовый', '70', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(12, 'Торты', 'Морковный', '130', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(13, 'Торты', 'Мороженное', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(14, 'Торты', 'Мулатка ', '120', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(15, 'Торты', 'Му-Му', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(16, 'Торты', 'Наполеон ', '90', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(17, 'Торты', 'Нутелла', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов\r\n', 0),
(18, 'Торты', 'Полночь', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(19, 'Торты', 'Прага', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(20, 'Торты', 'Райский сад', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(21, 'Торты', 'Рафаэлло', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(22, 'Торты', 'Сказка ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(23, 'Торты', 'Ферреро рошер', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(24, 'Торты', 'Фруктовый  ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(25, 'Торты', 'Фруктовый сад ', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(26, 'Торты', 'Фрутелла', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(27, 'Торты', 'Царский ', '120', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(28, 'Торты', 'Цезарь ', '170', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(29, 'Торты', 'Шоколадный Орео', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(30, 'Торты', 'Шоколадный трюфель', '170', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(31, 'Торты', 'Шоколандия', '100', '', 'Торт создан по оригинальной рецептуре из высококачественных ингредиентов', 0),
(32, 'Десерты', 'Афганка (наполеон)', '14', '', 'Песочное тесто со сливочным кремом', 0),
(33, 'Десерты', 'Муссовый \'Белый бархат\'', '20', '', 'Лёгкая взбитая масса со смородиной ', 0),
(34, 'Десерты', 'Муссовый \"Вишнёвый\"', '20', '', 'Лёгкая взбитая масса с вишней ', 0),
(35, 'Десерты', 'Вишнёвый тирамису', '20', '', 'Сыр маскарпоне с вишней', 0),
(36, 'Десерты', 'Вупи Пай', '15', '', 'Медовое тесто с сыром маскарпоне', 0),
(37, 'Десерты', 'Дамские пальчики (белые)', '75', '', 'Белый шоколад с грецким орехом', 0),
(38, 'Десерты', 'Дамские пальчики (шоколадные)', '75', '', 'Шоколадный с фисташкой', 0),
(39, 'Десерты', 'Заварной', '3', '', 'С заварным кремом', 0),
(40, 'Десерты', 'Муссовый \"Йогуртовый\"', '20', '', 'Лёгкая взбитая масса с йогуртом', 0),
(41, 'Десерты', 'Капкейки ванильные', '6', '', 'С ванильной начинкой ', 0),
(42, 'Десерты', 'Капкейки шоколадные', '6', '', 'С шоколадной начинкой', 0),
(43, 'Десерты', 'Десерт Карамелька', '6', '', 'Карамельный с грецким орехом', 0),
(44, 'Десерты', 'Муссовый \"Клубничный\"', '20', '', 'Лёгкая взбитая масса с клубникой', 0),
(45, 'Десерты', 'Корзинка \"Тоффи\"', '21', '', 'Шоколадная корзинка с нугой и с трюфелем', 0),
(46, 'Десерты', 'Круассаны', '15', '', 'Из слоённого теста, с разными начинками', 0),
(47, 'Десерты', 'Макароны', '9', '', 'Из миндальной муки, с разными начинками', 0),
(48, 'Десерты', 'Медовик', '14', '', 'Медовое тесто с карамелью и с со сливками', 0),
(49, 'Десерты', 'Миндальные корзинки', '5', '', 'Песочные корзинки с карамелью и орехом', 0),
(50, 'Десерты', 'Десерт Морковный', '15', '', 'Пряный и нежный тортик с морковью', 0),
(51, 'Десерты', 'Муссовый \'\'Сникерс\"', '20', '', 'Лёгкая взбитая масса, с карамелью и арахисом', 0),
(52, 'Десерты', 'Намелака ', '20', '', 'Шоколадный бисквит с намелакой', 0),
(53, 'Десерты', 'Наполеон (классический)', '14', '', 'Слоённое тесто с заварным кремом ', 0),
(54, 'Десерты', 'Муссовый \'\'Облачко\'\' ', '23', '', 'Лёгкая взбитая масса с мангой и маракуей', 0),
(55, 'Десерты', 'Опера', '20', '', 'Из миндальной муки, с шоколадной начинкой', 0),
(56, 'Десерты', ' Карамельный бум', '20', '', 'Бисквитный, с карамелью и прослойка муссовая', 0),
(57, 'Десерты', 'Фисташковый', '24', '', 'Бисквитный, с фисташкой и со сливками', 0),
(58, 'Десерты', 'Синнабоны', '7', '', 'Горячая булочка с корицей', 0),
(59, 'Десерты', 'Тирамису (классический)', '18', '', 'Нежный итальянский десерт со вкусом кофе', 0),
(60, 'Десерты', 'Чёрный лес', '20', '', 'Вишнёвый торт шоколадный, с лесными ягодами', 0),
(61, 'Десерты', 'Муссовый \'\'Три шоколада\'\'', '20', '', 'Лёгкая взбитая масса с тремя видами шоколада', 0),
(62, 'Десерты', 'Муссовый \'\'Сердечко\'\'', '20', '', 'Лёгкая взбитая масса с малиной', 0),
(63, 'Десерты', 'Муссовый \'\'Шарик\'\'', '20', '', 'Лёгкая взбитая масса с шоколадом и орехом', 0),
(64, 'Десерты', 'Тарталетка \'\'Вишнёвый\'\'', '15', '', 'Меренговые корзинки с вишнёвой начинкой', 0),
(65, 'Десерты', 'Тарталетка \'\'Лиммоный\'\'', '15', '', 'Меренговые корзинки с лимонным курдом', 0),
(66, 'Десерты', 'Тарталетка \'\'Шоколадный\'\'', '15', '', 'Цельно-шоколадные корзинки ', 0),
(67, 'Десерты', 'Творожная ягода ', '16', '', 'Творожнная масса с ягодами', 0),
(68, 'Десерты', 'Фантазия', '15', '', 'С белгийским шоколадом', 0),
(69, 'Десерты', 'Фруктовые корзинки ', '5', '', 'Песочная корзинка, с фруктами и ягодами', 0),
(70, 'Десерты', 'Чизкейки ', '25', '', 'Творожный сыр и разные вкусовые начинки ', 0),
(71, 'Десерты', 'Чизкейк \'\'Орео\'\'', '23', '', 'Шоколадный бисквит с творожным сыром и \'\'Орео\'\'', 0),
(72, 'Десерты', 'Муссовый \'\'Чёрный лес\'\'', '18', '', 'Лёгкая взбитая масса с вишней ', 0),
(73, 'Холодные напитки', 'Ice coffee Американо', '15', '', 'Холодное кофе на основе Эспрессо и льда', 0),
(74, 'Холодные напитки', 'Ice coffee Капучино', '20', 'https://img.freepik.com/premium-photo/milk-being-poured-into-iced-coffee-on-a-dark-table_118631-2003.jpg?w=2000', 'Холодное кофе на основе эспрессо, молока и льда', 0),
(75, 'Холодные напитки', 'Ice coffee Латте', '20', 'https://telegra.ph/file/8fea0965141f998e90b07.png', 'Холодное кофе на основе эспрессо, молока и льда', 0),
(76, 'Холодные напитки', 'Ice coffee Раф', '25', '', 'Холодное кофе на основе эспрессо, сливок и ванили ', 0),
(77, 'Холодные напитки', 'Ice coffee Бамбл', '25', '', 'Холодное кофе на основе эспрессо и апельсина', 0),
(78, 'Холодные напитки', 'Вода OBI ZULOL ', '6', '', 'Холодный напиток 0,5л', 0),
(79, 'Холодные напитки', 'Вода RC COLA', '8', '', 'Холодный напиток 0,5л', 0),
(80, 'Холодные напитки', 'Сок Rich', '13', '', 'Холодный напиток 0,2л', 0),
(81, 'Горячие напитки', 'Кофе РАФ', '20', '', 'На основе эспрессо, сливок и ванили', 0),
(82, 'Горячие напитки', 'Кофе РАФ 0,4л', '25', '', 'На основе эспрессо, сливок и ванили 0,4л', 0),
(83, 'Горячие напитки', 'Кофе Американо', '10', '', 'На основе эспрессо и воды', 0),
(84, 'Горячие напитки', 'Кофе Американо (double)', '14', '', 'На основе двойного эспрессо и воды', 0),
(85, 'Горячие напитки', 'Кофе Эспрессо', '13', '', 'На основе кофейного сока', 0),
(86, 'Горячие напитки', 'Кофе Капучино ', '15', '', 'На основе эспрессо и вспененного молока', 0),
(87, 'Горячие напитки', 'Кофе Капучино 0,4л', '18', '', 'На основе эспрессо и вспененного молока 0,4л', 0),
(88, 'Горячие напитки', 'Кофе Капучино (double)', '17', '', 'На основе двойного эспрессо и вспененного молока', 0),
(89, 'Горячие напитки', 'Кофе Латте', '16', '', 'На основе эспрессо и вспененного молока', 0),
(90, 'Горячие напитки', 'Кофе Латте 0,4л', '19', '', 'На основе эспрессо и вспененного молока 0,4л', 0),
(91, 'Горячие напитки', 'Кофе Макиато ', '16', '', 'На основе двойного эспрессо и вспененного молока', 0),
(92, 'Горячие напитки', 'Кофе Макиато 0,4л', '20', '', 'На основе двойного эспрессо и вспененного молока 0,4л', 0),
(93, 'Горячие напитки', 'Кофе Мокаччино', '18', '', 'На основе эспрессо, шоколада и молока', 0),
(94, 'Горячие напитки', 'Кофе Мокаччино 0,4л', '21', '', 'На основе эспрессо, шоколада и молока 0,4л', 0),
(95, 'Горячие напитки', 'Кофе Романо ', '16', '', 'На основе эспрессо и лимона', 0),
(96, 'Горячие напитки', 'Чай - Облепиховый', '23', '', 'Ароматный чай с облепихой 0,8л', 0),
(97, 'Горячие напитки', 'Чай - Лимон', '12', '', 'Чай с лимоном', 0),
(98, 'Горячие напитки', 'Чай - Молочный Улун', '15', '', 'Лиственный ароматный чай со вкусом молока', 0),
(99, 'Горячие напитки', 'Чай - Шафран', '47', '', 'Чай с шафраном, имбирём и мёда', 0),
(100, 'Горячие напитки', 'Чай - Ягодный', '23', '', 'Ароматный чай с разными ягодами и с лимоном', 0),
(101, 'Горячие напитки', 'Чай - Имбирь', '20', '', 'Ароматный чай на основе имбиря и мёда', 0),
(102, 'Горячие напитки', 'Чайные напитки', '11', '', 'Ароматные чаи с разными вкусами ', 0),
(103, 'Горячие напитки', 'Чай - чёрный', '7', '', 'Лиственный чёрный чай', 0),
(104, 'Горячие напитки', 'Чай - зелёный', '7', '', 'Лиственный зелёный чай', 0),
(106, 'Торты', 'хеллоу', '5', 'https://google.com', 'sfd', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `profiles`
--

CREATE TABLE `profiles` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username_telegram` text NOT NULL,
  `fio` text NOT NULL,
  `address` text NOT NULL,
  `phone` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `profiles`
--

INSERT INTO `profiles` (`id`, `user_id`, `username_telegram`, `fio`, `address`, `phone`) VALUES
(16, 1883517936, 'muhammadsaid_vosidov', 'G', 'st. 279', '+992400084277');

-- --------------------------------------------------------

--
-- Структура таблицы `shopping_list`
--

CREATE TABLE `shopping_list` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `username` varchar(50) NOT NULL,
  `product` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `price` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `shopping_list`
--

INSERT INTO `shopping_list` (`id`, `user_id`, `username`, `product`, `price`, `amount`) VALUES
(16, '828354079', 'nazirjon_ismoiljonov', 'Ice coffee Латте', 20, 1),
(20, '1883517936', 'muhammadsaid_vosidov', 'Белый трюфель', 100, 2);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `on_time`
--
ALTER TABLE `on_time`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `profiles`
--
ALTER TABLE `profiles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `shopping_list`
--
ALTER TABLE `shopping_list`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `on_time`
--
ALTER TABLE `on_time`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=140;

--
-- AUTO_INCREMENT для таблицы `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT для таблицы `profiles`
--
ALTER TABLE `profiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT для таблицы `shopping_list`
--
ALTER TABLE `shopping_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
