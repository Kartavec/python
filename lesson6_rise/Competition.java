package lesson6_rise;

public class Competition {

    public static void main(String[] args) {

        Cat Murka = new Cat("Murka");
        Cat Vaska = new Cat("Vaska");

        //Проверка допуска животного к разным соревнованиям
        Murka.run(500);
        Vaska.run(30);
        Murka.swim(10);
        Vaska.swim(100);
        Murka.jump(10);
        Vaska.jump(0.2);

        System.out.println();

        Dog Lopuh = new Dog("Lopuh");
        Dog Makadam = new Dog("Makadam");

        //Проверка допуска животного к разным соревнованиям
        Lopuh.run(2);
        Makadam.run(600);
        Lopuh.swim(2);
        Makadam.swim(30);
        Lopuh.jump(1);
        Makadam.jump(30);
    }
}
