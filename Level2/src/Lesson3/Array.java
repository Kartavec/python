package Lesson3;

/*
Создать массив с набором слов (10-20 слов, должны встречаться повторяющиеся).
Найти и вывести список уникальных слов, из которых состоит массив
(дубликаты не считаем). Посчитать сколько раз встречается каждое слово.
*/

import java.util.*;

public class Array {
    public static void main(String[] args) {

        String[] words = {"Ivan", "orange", "Ivan", "orange",
                        "table", "green", "black", "QWERTY",
                        "green", "orange", "orange", "table",
                        "green", "black", "table", "green"};

        HashMap<String, Integer> uniqueWords = new HashMap<>();

        for (String x : words) {
            uniqueWords.put(x, uniqueWords.getOrDefault(x,0)+1);
        }
        System.out.println(uniqueWords);
    }
}
