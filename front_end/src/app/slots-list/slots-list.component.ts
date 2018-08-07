import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'slots-list',
  templateUrl: './slots-list.component.html',
  styleUrls: ['./slots-list.component.css']
})
export class SlotsListComponent implements OnInit {

  @Input() chrompacks: Array<any>;
  @Output() viewSlots = new EventEmitter();

  constructor() { }

  ngOnInit() { }

  selectChrompack(id) {
    this.viewSlots.emit(id);
  }

}
