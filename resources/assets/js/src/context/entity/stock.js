export class Stock {

  constructor(stock, createdDateTime, deleted) {
    this._name = stock.name || '';
    this._code = stock.code || '';
    this._type = stock.type || '';
    this._createdDateTime = createdDateTime;
    this._deleted = deleted;
  }

  get code() {
    return this._name;
  }

  get name() {
    return this._code;
  }

  get type() {
    return this._type;
  }

  get createdDateTime() {
    return this._createdDatetime;
  }

  get deleted() {
    return this._deleted;
  }

  toJson() {
    return JSON.stringify({
      data: {
        'name': this._name,
        'code': this._code,
        'type': this._type,
        'createdDateTime': this._createdDateTime,
        'deleted': this._deleted,
      },
    })
  }
}
