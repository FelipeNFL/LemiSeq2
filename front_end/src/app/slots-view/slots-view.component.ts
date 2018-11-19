import { ManagerSlots } from '../services/manager-slots';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'slots-view',
  templateUrl: './slots-view.component.html',
  styleUrls: ['./slots-view.component.css']
})
export class SlotsViewComponent implements OnInit {

  @Input() slots: any;
  @Input() isSelectable: boolean;
  @Output() eventSelectSlot: EventEmitter<any> = new EventEmitter();

  constructor() {}
  
  ngOnInit() {}

  getColumns() {
    if (this.slots) {
      return new ManagerSlots(this.slots).getColumns();
    }
  }

  getLines() {
    if (this.slots) {
      const lines = Object.keys(this.slots).sort();
      return lines.map(line => { return {number: line, content: this.slots[line]} });
    }
  }

  getClass(content) {

    const state = content ? content.state + ' slot' : 'not-found';
    let classSlot = state + ' slot' ;
    
    if(this.isSelectable && state != 'not-found') {
      classSlot += ' selectable';
    }

    return classSlot;
  }

  select(letter, number, content) {

    if (this.isSelectable && content.state != 'not-found') {
      this.eventSelectSlot.emit({ letter, number, content});
    }
  }

  getTitle(content) {

    if (!content) {
      return '';
    }

    if (content.state === 'busy') {
      return content.subject;
    }
  }
}
