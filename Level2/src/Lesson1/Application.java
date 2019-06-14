package Lesson1;

public class Application {

    public static void main(String[] args) {

        // Создаем полосу препятствий
        Course c = new Course(new Wall(5),
                new RunningTrack(25)
        );

        // Создаем команду
        Team team = new Team("First",
                new Person("Rita"),
                new Cat("Murka"),
                new Robot("Gold"),
                new Robot("Silver"));

        c.doIt(team); // Просим команду пройти полосу

        System.out.println();
        team.showResults(); // Показываем результаты


    }
}

