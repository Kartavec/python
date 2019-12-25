package Lesson4.Swing;

/*
Создать окно для клиентской части чата: большое текстовое поле для отображения переписки
        в центре окна. Однострочное текстовое поле для ввода сообщений и кнопка
        для отсылки сообщений на нижней панели. Сообщение должно отсылаться
        либо по нажатию кнопки на форме, либо по нажатию кнопки Enter.
        При «отсылке» сообщение перекидывается из нижнего поля в центральное.

        Если на JavaFX, то дополнение к чату
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ChatAnna extends JFrame{
    JPanel jpN = new JPanel(new GridLayout());
    JPanel jpS = new JPanel(new GridLayout());

    JButton button = new JButton("Send"); //Кнопка
    JTextArea textArea = new JTextArea(); //Многострочное поле
    JScrollPane scroll = new JScrollPane(textArea); //Полоса прокрутки. Надевается на многострочное поле
    JTextField textField = new JTextField(); //Текстовое поле

    JMenuBar mainMenu = new JMenuBar(); //Главное меню. Располагается в верхней части окна
    JMenu mFile = new JMenu("File"); //Меню, которое содержит внутри себя JMenuItem
    JMenu mHelp = new JMenu("Help");
    JMenuItem miFileExit = new JMenuItem("Exit");
    JMenuItem miHelpAbout = new JMenuItem("About");

    ChatAnna() {
        super("Chat Anna");
//        setSize(100, 100);
        setMinimumSize(new Dimension(300, 400));

        textArea.setLineWrap(true); //Перенос текста на новую строку
        textArea.setWrapStyleWord(true); //Перенос текста по словам (целиком)
        textArea.setEditable(false); //Блокируем пользователю возможность вводить данные в поле с выводом сообщений

        //При нажатии кнопки Send сообщение отправится
        button.addActionListener(e -> {
            sendMessage();
        });

        //При нажатии Enter сообщение отправится
        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) sendMessage();
            }
        });

        jpN.add(scroll); //Добавляем в верхнее поле прокрутку в которой завернуто текстовое поле
        jpS.add(textField); //Добавляем в нижнее поле поле ввода
        jpS.add(button); //Добавляем в нижнее поле поле кнопку

        add(jpN); //В панель добавляем верхнее поле
        add("South", jpS);  //В панель добавляем нжее поле c указанием расположения

        //Рисуем меню
        setJMenuBar(mainMenu);
        mainMenu.add(mFile);
        mainMenu.add(mHelp);
        mFile.add(miFileExit);
        mHelp.add(miHelpAbout);
        miFileExit.addActionListener(e -> System.exit(0));
        miHelpAbout.addActionListener(e -> JOptionPane.showMessageDialog(null,"Chat Anna version 1.0", "About", JOptionPane.INFORMATION_MESSAGE));

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); //Расположить окно приложения по центру монитора
        setVisible(true);
    }

    //Вывод сообщения
    void sendMessage() {
        String out = textField.getText();
        textArea.append(getTime() + " : " + out + "\n" + "\n");
        textField.setText(""); //Очистка поля после ввода сообщения
    }

    //Получение текущего времени
    public String getTime() {
        return new SimpleDateFormat("YYYY" + " / " + "HH:mm:ss").format(new Date());
    }
}

class ApplicaionStart {
    public static void main(String[] args) {
        new ChatAnna();
    }
}
