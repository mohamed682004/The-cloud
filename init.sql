USE cloudy_members
CREATE TABLE member
(
    id BIGINT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    CGPA DECIMAL NOT NULL,
    CONSTRAINT CGPA_range CHECK(CGPA >= 0 AND CGPA <= 4.0),
    CONSTRAINT age_range CHECK(age >= 18 and age <= 22)
);

INSERT INTO member
VALUES
    (22010333, 'Khalil Elemam', 19, 3.78),
    (22010211, 'Muhammed Emran', 19, 3.2),
    (22010022, 'Ahmed AdbelHamed', 19, 3.1),
    (22010215, 'Muhammed Gamal', 19, 3.2);