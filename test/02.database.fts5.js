"use strict";
const Database = require("../lib");

describe("Database#fts5()", function () {
  beforeEach(function () {
    this.db = new Database(util.next());
  });

  afterEach(function () {
    this.db.close();
  });

  it("should allow creating a table with snowball tokenizer", function () {
    expect(() =>
      this.db.exec(
        "CREATE VIRTUAL TABLE test USING fts5 (content, tokenize = \"synonyms phrases snowball stopwords unicode remove_diacritics 2 tokenchars '-/'''\");"
      )
    ).to.not.throw(TypeError);
    expect(() =>
      this.db.exec("INSERT INTO test (content) VALUES ('Testing testing 123');")
    ).to.not.throw(TypeError);
  });
});
