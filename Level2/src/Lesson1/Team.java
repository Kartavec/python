package Lesson1;

public class Team {
    private String title;
    private Actions[] members;

    public Actions[] getMembers() {
        return members;
    }

    public Team(String title, Actions... members) {
        this.title = title;
        this.members = members;
    }

    public void showResults() {
        System.out.println("Участники команды " + title + ", успешно прошедшие все препятствия:");
        for (Actions a: members) {
            if(a.isOnDistance()) {
                a.info();
            }

        }
    }
}
