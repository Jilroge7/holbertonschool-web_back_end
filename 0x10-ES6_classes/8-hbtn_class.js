export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  Number() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
