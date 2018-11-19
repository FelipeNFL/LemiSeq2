import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { SubjectService } from '../services/subject.service';
import { AlertsService } from '../services/alerts.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-subject',
  templateUrl: './subject.component.html',
  styleUrls: ['./subject.component.css']
})
export class SubjectComponent implements OnInit {

  refreshMetricsSubscription: Subscription
  slots: any;
  idChrompack: string;
  selectedTitle: string;
  title: string;
  subjects: Array<string>;

  constructor(private subjectService: SubjectService,
              private alerts: AlertsService,
              private route: ActivatedRoute) {}

  ngOnInit() {

    this.idChrompack = this.route.snapshot.params['id_chrompack'];

    if(this.idChrompack){
      this.fillSlots();
    }
    else {
      this.alerts.error('Chrompack ID not found. Try to select chrompack again!');
    }
  }

  fillSlots(){
    this.subjectService.getMatrixAll(this.idChrompack).subscribe(result => {
      this.slots = result;
    }, err => {
      this.alerts.error('Error to display slots array', err);
    });
  }

  selectSubject(title) {
    this.selectedTitle = title;
  }

  selectSlot(slotObj) {

    const content = slotObj.content;
    const state = content.state;
    const slot = slotObj.letter + slotObj.number;

    if (state == 'free') {

      this.subjectService.addSubjectToSlot(this.selectedTitle, slot, this.idChrompack).subscribe(() => {
        this.fillSlots();
      }, err => {
        this.alerts.error('Error to update slot', err);
      });

      return;
    }

    if (content.subject == this.selectedTitle) {
      this.subjectService.cleanSlot(slot, this.idChrompack).subscribe(() => {
        this.fillSlots();
      }, err => {
        this.alerts.error('Error to clean slot', err);
      });

      return;
    }

    this.alerts.warning('Slot already allocated to other subject');
  }
}
