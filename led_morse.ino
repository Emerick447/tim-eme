const int LED = 13;

String lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
String morse[] = {
  ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
  "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
  "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
  "-.--", "--..",
  "-----", ".----", "..---", "...--", "....-", ".....",
  "-....", "--...", "---..", "----."
};

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);

  Serial.println("Entrez un texte :");
}

void loop() {
  if (Serial.available()) {
    String texte = Serial.readStringUntil('\n');
    texte.toUpperCase();

    Serial.print("Morse : ");
    Serial.println(texte);

    for (int i = 0; i < texte.length(); i++) {
      char c = texte[i];

      if (c == ' ') {
        delay(1400);
        continue;
      }

      int index = lettres.indexOf(c);

      if (index >= 0) {
        String code = morse[index];

        for (int j = 0; j < code.length(); j++) {
          if (code[j] == '.') {
            digitalWrite(LED, HIGH);
            delay(200);
            digitalWrite(LED, LOW);
            delay(200);
          }
          else if (code[j] == '-') {
            digitalWrite(LED, HIGH);
            delay(600);
            digitalWrite(LED, LOW);
            delay(200);
          }
        }

        delay(600);
      }
    }

    Serial.println("Termine.");
  }
}
