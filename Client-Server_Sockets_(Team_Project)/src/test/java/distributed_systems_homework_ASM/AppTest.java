package distributed_systems_homework_ASM;

import junit.framework.*;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import java.io.IOException;
import java.io.File;
import java.net.URL;
import java.net.URI;
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
        System.out.println("Running test: testApp");

        fileString = getClass().getClassLoader().getResource("json.txt").toString().split(":")[1];

        Server s = new Server(new File(fileString));
        s.setVerbose(true);

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
    }

    //@Test
    public void testInvalidinputForGet() throws IOException
    {
        System.out.println("Running test: testInvalidinputForGet");

        Server s = new Server(new File(fileString));
        s.setVerbose(true);

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

    public void testInvalidinputForAdd() throws IOException {
        System.out.println("Running test: testInvalidinputForAdd");
        
        Server s = new Server(new File(fileString));
        s.setVerbose(true);

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
