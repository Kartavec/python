package Lesson3;

/*
Написать простой класс ТелефонныйСправочник, который хранит в себе список
фамилий и телефонных номеров. В этот телефонный справочник с помощью метода add()
можно добавлять записи. С помощью метода get() искать номер телефона по фамилии.
        Следует учесть, что под одной фамилией может быть несколько телефонов
        (в случае однофамильцев), тогда при запросе такой фамилии
должны выводиться все телефоны.
*/

import java.util.HashMap;
import java.util.HashSet;

public class PhoneBook {

    HashMap<String, HashSet<String>> pb;

    public PhoneBook() {
        this.pb = new HashMap<>();
    }

    public void add(String name, String phone) {
        HashSet<String> book = pb.getOrDefault(name, new HashSet<>());
        book.add(phone);
        pb.put(name, book);
    }

    public void get(String name) {
        System.out.println(name + " : " + pb.getOrDefault(name, new HashSet<>()));
    }
}
