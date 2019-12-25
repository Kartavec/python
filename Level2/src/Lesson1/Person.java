package Lesson1;

public class Person implements Actions {

    private int heightRestriction;
    private int lengthRestriction;

    String name;
    boolean active = true;

    public Person(String name) {
        this.name = name;
        this.heightRestriction = 5;
        this.lengthRestriction = 30;
    }

    @Override
    public void run(int length) {
        if (length <= lengthRestriction) {
            System.out.println("Человек " + name + " успешно пробежал " + length + " метра(-ов)");
        }
        else {
            System.out.println("Человек " + name + " не смог пробежать " + length + " метра(-ов)");
            active = false;
        }
    }

    @Override
    public void jump(int height) {
        if (height <= heightRestriction) {
            System.out.println("Человек " + name + " успешно прыгнул на " + height + " метра(-ов)");
        }
        else {
            System.out.println("Человек " + name + " не смог прыгнуть на " + height + " метра(-ов)");
            active = false;
        }
    }

    @Override
    public boolean isOnDistance() {
        return active;
    }

    @Override
    public void info() {
        System.out.println(name);
    }
}
