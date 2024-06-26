import { objValidation as validateObj } from "../validation/objValidation.js";


class GameUser {
  static mustHaveKeys = ["id", "username"];

  constructor(id, username) {
    this.id = id;
    this.username = username;
  }

  static createGameUserFromObj(obj) {
    validateObj(GameUser, obj);
    return new GameUser(obj.id, obj.username);
  }
}

class GamePlayer {
  static mustHaveKeys = ["user", "score"];

  constructor(user, score) {
    this.user = GameUser.createGameUserFromObj(user);
    this.score = score;
  }

  static createGamePlayerFromObj(obj) {
    validateObj(GamePlayer, obj);
    validateObj(GameUser, obj.user);
    return new GamePlayer(obj.user, obj.score);
  }

  draw() {};
  update() {};
}

export { GamePlayer };
