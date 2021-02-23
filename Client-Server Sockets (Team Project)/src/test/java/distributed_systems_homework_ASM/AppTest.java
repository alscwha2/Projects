package distributed_systems_homework_ASM;

import junit.framework.*;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import java.io.IOException;
import java.io.File;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.*;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    private static String fileString;
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp() throws IOException
    {
        fileString = System.getProperty("fileName");
        new Thread(() -> {
            try{
                Server s = new Server(new File(fileString));
                s.setVerbose(true);
            } catch (IOException e) {
                System.err.println("TESTCLASS CAUGHT: " + e.getClass() + " : " + e.getMessage());
            }
        }).start();
        Client c = new Client();
        c.setVerbose(true);

        c.add("COM", 7755003, "MYADDEDCLASS");
        c.add("BIO", 12344, "BIOBIOBIOBIOBIOBIO");
        c.get("BIO");
        c.delete(12344);
        c.get("BIO");
        c.delete(12344);
        c.delete(12344);
        c.get("COM");
        c.delete(1233567);
        c.delete(7755003);
        c.shutDownServer();
        assertTrue( true );
    }

    //@Test
    public void testInvalidinputForGet() {
        new Thread(() -> {
            try{
                Server s = new Server(new File(fileString));
                s.setVerbose(true);
            } catch (IOException e) {
                System.err.println("TESTCLASS CAUGHT: " + e.getClass() + " : " + e.getMessage());
            }
        }).start();
        Client c = new Client();
        c.setVerbose(true);

        try {
            c.get("PSY");
            c.add("PSY", 123244, "sommersault");
            fail("Expected an IllegalArgumentException to be thrown");
        } catch (IllegalArgumentException e) {
            assertThat(e.getMessage(), org.hamcrest.CoreMatchers.is("Only \"COM\", \"MAT\", and \"BIO\" are valid inputs."));
        }
        c.shutDownServer();
    }

    public void testInvalidinputForAdd()
    {
        new Thread(() -> {
            try{
                Server s = new Server(new File(fileString));
                s.setVerbose(true);
            } catch (IOException e) {
                System.err.println("TESTCLASS CAUGHT: " + e.getClass() + " : " + e.getMessage());
            }
        }).start();
        Client c = new Client();
        c.setVerbose(true);

        try {
            c.add("PSY", 123244, "sommersault");
            fail("Expected an IllegalArgumentException to be thrown");
        } catch (IllegalArgumentException e) {
            assertThat(e.getMessage(), org.hamcrest.CoreMatchers.is("Only \"COM\", \"MAT\", and \"BIO\" are valid inputs."));
        }
        c.shutDownServer();
    }
}
