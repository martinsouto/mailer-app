instructions = [
    'DROP TABLE IF EXISTS mail;',
    """
        CREATE TABLE mail (
            id INT PRIMARY KEY AUTO_INCREMENT,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        );
    """
]