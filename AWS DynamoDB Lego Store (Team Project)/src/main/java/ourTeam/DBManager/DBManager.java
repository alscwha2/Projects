package ourTeam;

import java.util.Set;

interface DBManager {
    Integer getPartCount(int set, String part);

    void decrementSet(int set, int amount);

    Set<String> getParts(int set);

    void incrementPart(int set, String part, int amount);

    Integer getSetCount(int set);

    void incrementSet(int set, int amount);

    void decrementPart(int set, String part, int amount);
}
