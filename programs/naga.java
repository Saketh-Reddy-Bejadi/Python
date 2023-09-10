import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class QuizApplication extends JFrame implements ActionListener {
 private JLabel questionLabel;
 private JRadioButton[] options;
 private JButton nextButton;
 private ButtonGroup buttonGroup;
 private int currentQuestion;
 private int score;
 private String[] questions = {
 "1. Who is the main character in One-Piece?",
 "2. Who painted the Mona Lisa?",
 "3. What is the currency of Japan?",
 "4. how many swords used by Zoro?",
 "5. Who wrote the play 'Romeo and Juliet'?"
 };
 private String[][] optionsList = {
 {"a. Luffy", "b. Naruto", "c. Goku", "d. ash"},
 {"a. Michelangelo", "b. Leonardo da Vinci", "c. Pablo Picasso", "d. Vincent van Gogh"},
 {"a. Yen", "b. Euro", "c. Dollar", "d. Pound"},
 {"a. 2", "b. 1", "c. 4", "d. 3"},
 {"a. William Shakespeare", "b. Oscar Wilde", "c. George Bernard Shaw", "d. Charles Dickens"}
 };
 private int[] correctAnswers = {1, 2, 1, 4, 1};

public QuizApplication() {
 super("Quiz Application");
 setSize(500, 400);
 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 setLocationRelativeTo(null);
 setLayout(new BorderLayout());
 JPanel questionPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
 questionLabel = new JLabel(questions[currentQuestion]);
 questionLabel.setFont(new Font("Arial", Font.PLAIN, 16));
 questionPanel.add(questionLabel);
 JPanel optionsPanel = new JPanel(new GridLayout(4, 1));
 options = new JRadioButton[4];
 buttonGroup = new ButtonGroup();
 for (int i = 0; i < 4; i++) {
 options[i] = new JRadioButton(optionsList[currentQuestion][i]);
 options[i].setFont(new Font("Arial", Font.PLAIN, 14));
 buttonGroup.add(options[i]);
 optionsPanel.add(options[i]);
 }
 JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
 nextButton = new JButton("Next");
 nextButton.setFont(new Font("Arial", Font.BOLD, 14));
 nextButton.addActionListener(this);
 buttonPanel.add(nextButton);
 add(questionPanel, BorderLayout.NORTH);
 add(optionsPanel, BorderLayout.CENTER);
 add(buttonPanel, BorderLayout.SOUTH);
 setVisible(true);
 }


 public void actionPerformed(ActionEvent e) {
 if (currentQuestion < questions.length - 1) {
 checkAnswer();
 currentQuestion++;
 updateQuestion();
 } else {
 checkAnswer();
 showResult();
 dispose();
 }
 }
 private void checkAnswer() {
 for (int i = 0; i < 4; i++) {
 if (options[i].isSelected() && i + 1 == correctAnswers[currentQuestion]) {
 score++;
 break;
 }
 }
 }
 private void updateQuestion() {
 questionLabel.setText(questions[currentQuestion]);
 buttonGroup.clearSelection();
 for (int i = 0; i < 4; i++) {
 options[i].setText(optionsList[currentQuestion][i]);
 }
 }
 private void showResult() {
 JOptionPane.showMessageDialog(this, "Quiz complete!\nYour score: " + score + "/" + 
questions.length,
 "Quiz Result", JOptionPane.INFORMATION_MESSAGE);
 }


public static void main(String[] args) {
 SwingUtilities.invokeLater(new Runnable() {
 public void run() {
 new QuizApplication();
 }
 });
 }
}