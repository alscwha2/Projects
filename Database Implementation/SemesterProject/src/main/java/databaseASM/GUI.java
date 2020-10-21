package databaseASM;
import javax.swing.*;

import net.sf.jsqlparser.JSQLParserException;

import java.awt.*;
import java.io.IOException;
/**
* Created by mordechaichern on 1/30/16.
* For testing
*/
public class GUI extends JFrame
{
	String userWord = "";
	JTextField userInput = new JTextField(50);
	JButton submit = new JButton("Submit");
	JTextArea myOutput;
	CanExecute executor;

	public GUI(CanExecute executor)
	{
		super("DataBase");
		this.executor = executor;
		JPanel centerPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 15));
		setSize(WIDTH, HEIGHT);
		setDefaultCloseOperation(EXIT_ON_CLOSE);

		// This center the window on the screen
		submit.addActionListener((e) -> {submitAction();});
		centerPanel.add(userInput);
		JPanel southPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 15));
		southPanel.add(submit);
		myOutput = new JTextArea(50,30);
		myOutput.setVisible(true);
		southPanel.add(myOutput);
		Box theBox = Box.createVerticalBox();
		theBox.add(Box.createVerticalStrut(10));
		theBox.add(centerPanel);
		theBox.add(Box.createVerticalStrut(10));
		theBox.add(southPanel);
		add(theBox);
		setSize(500, 500);
		setLocationRelativeTo(null);
	}
	
	private void submitAction()
	{
		userWord = userInput.getText();
		try{
			Table table = executor.execute(userWord);
			myOutput.setText(table.toString());
		}
		catch (Exception e){
			myOutput.setText(e.getMessage());
		}
	}
	
	public static void main(String[] args) throws IOException, JSQLParserException
	{
		GUI gui = new GUI(new DataBase());
		gui.setVisible(true);
	}
}