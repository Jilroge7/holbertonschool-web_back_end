export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (this.evacuationWarningMessage === undefined) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(Sqft) {
    this._sqft = Sqft;
  }
}
