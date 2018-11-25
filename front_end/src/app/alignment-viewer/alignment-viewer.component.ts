import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-alignment-viewer',
  templateUrl: './alignment-viewer.component.html',
  styleUrls: ['./alignment-viewer.component.css']
})
export class AlignmentViewerComponent implements OnInit {

  constructor(public activeModal: NgbActiveModal) {}

  @Input() sequenceBase: any;
  @Input() sequencesToAlign: Array<any>;

  ngOnInit() {}

  close() {
    this.activeModal.close();
  }
}
