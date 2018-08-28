import { ManagerSlots } from '../services/manager-slots';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'slots-view',
  templateUrl: './slots-view.component.html',
  styleUrls: ['./slots-view.component.css']
})
export class SlotsViewComponent implements OnInit {

  @Input() slots: any;

  constructor() {}
  
  ngOnInit() {}

  getColumns() {
    if (this.slots) {
      return new ManagerSlots(this.slots).getColumns();
    }
  }

  getLines() {
    if (this.slots) {
      const lines = Object.keys(this.slots);
      return lines.map(line => { return {number: line, content: this.slots[line]} });
    }
  }

}
