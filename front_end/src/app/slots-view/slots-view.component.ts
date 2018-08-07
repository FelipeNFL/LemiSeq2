import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'slots-view',
  templateUrl: './slots-view.component.html',
  styleUrls: ['./slots-view.component.css']
})
export class SlotsViewComponent implements OnInit {

  @Input() settings: Array<Array<boolean>>;

  constructor() { }

  ngOnInit() {
  }

  getLetter(index) {
    return String.fromCharCode(97 + index);
  }

}
