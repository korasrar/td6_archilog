export class QuizProvider {
  constructor(apiEndpoint) {
    this.apiEndpoint = apiEndpoint;
  }

  async getQuestionnaires() {
    const response = await fetch(this.apiEndpoint + "questionnaires");
    const json = await response.json();
    console.log("getQuestionnaires response:", json.questionnaires);
    return json.questionnaires;
  }

  async getQuestionnaire(idQuestionnaire) {
    const response = await fetch(
      this.apiEndpoint + "questionnaires/" + idQuestionnaire,
    );
    const json = await response.json();
    console.log("getQuestionnaire response:", json);
    return json;
  }

  async addQuestionnaire(questionnaire) {
    const response = await fetch(this.apiEndpoint + "questionnaires", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(questionnaire),
    });
    const json = await response.json();
    console.log("addQuestionnaire response:", json);
    return json;
  }

  async deleteQuestionnaire(idQuestionnaire) {
    await fetch(this.apiEndpoint + "questionnaires/" + idQuestionnaire, {
      method: "DELETE",
    });
  }

  async updateQuestionnaire(idQuestionnaire, updatedQuestionnaire) {
    const response = await fetch(
      this.apiEndpoint + "questionnaires/" + idQuestionnaire,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedQuestionnaire),
      },
    );
    return await response.json();
  }

  async getQuestions(idQuestionnaire) {
    const response = await fetch(
      this.apiEndpoint + "questionnaires/" + idQuestionnaire + "/questions",
    );
    return await response.json();
  }

  async addQuestion(idQuestionnaire, question) {
    const response = await fetch(
      this.apiEndpoint + "questionnaires/" + idQuestionnaire + "/questions",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(question),
      },
    );
    return await response.json();
  }

  async deleteQuestion(idQuestionnaire, idQuestion) {
    await fetch(
      this.apiEndpoint +
        "questionnaires/" +
        idQuestionnaire +
        "/questions/" +
        idQuestion,
      {
        method: "DELETE",
      },
    );
  }

  async updateQuestion(idQuestionnaire, idQuestion, updatedQuestion) {
    const response = await fetch(
      this.apiEndpoint +
        "questionnaires/" +
        idQuestionnaire +
        "/questions/" +
        idQuestion,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedQuestion),
      },
    );
    return await response.json();
  }

  async checkDoublonNomQuestionnaire(title) {
    const result = await this.getQuestionnaires();
    const existing = result.find((q) => q.title.toLowerCase() === title.toLowerCase());
    return !!existing;
  }
}
