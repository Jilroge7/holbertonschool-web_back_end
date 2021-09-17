import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = Currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(Amount) {
    this._amount = Amount;
  }

  get Currency() {
    return this._currency;
  }

  set Currency(Currency) {
    this._currency = Currency;
  }
}
