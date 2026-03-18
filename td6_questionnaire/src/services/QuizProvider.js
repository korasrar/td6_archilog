export class QuizProvider {
  constructor(apiEndpoint) {
    this.apiEndpoint = apiEndpoint;
  }

  async getQuestionnaires() {
    const response = await fetch(this.apiEndpoint + "questionnaires");
    return await response.json();
  }

  async getQuestionnaire(idQuestionnaire) {
    const response = await fetch(
      this.apiEndpoint + "questionnaires/" + idQuestionnaire,
    );
    return await response.json();
  }

  async addQuestionnaire(questionnaire) {
    const response = await fetch(this.apiEndpoint + "questionnaires", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(questionnaire),
    });
    return await response.json();
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
}
