class WorldBoard{
    constructor(tiles,weight,height){

    }
}

class Tile {
  constructor(type, url) {
    this.type = type;
    this.url = url;
  }
  getHtmlElement(){
      $(`<div class="col-1"></div>`)
  }
}
