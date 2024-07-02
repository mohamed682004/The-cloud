USE cloudy_members
CREATE TABLE member
(
    id BIGINT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    CGPA FLOAT NOT NULL,
    CONSTRAINT CGPA_range CHECK(CGPA >= 0 AND CGPA <= 4.0),
    CONSTRAINT age_range CHECK(age >= 18 and age <= 22)
);

INSERT INTO member
VALUES
    (1, 'Member One', 19, 4),
    (2, 'Member Two', 21, 4),
    (3, 'Member Three', 21, 4),
    (4, 'Member Four', 19, 4),
    (5, 'Member Five', 20, 4);
