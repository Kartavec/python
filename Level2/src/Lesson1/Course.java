package Lesson1;

public class Course {
    private Barrier[] barriers;

    public Course(Barrier... barriers) {
        this.barriers = barriers;
    }

    public void doIt(Team team) {
        for (Actions a: team.getMembers()) {
            for (Barrier b: barriers) {
                b.doIt(a);
                if (!a.isOnDistance()){
                    break;
                }
            }
        }
    }
}
