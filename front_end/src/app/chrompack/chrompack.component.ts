import { Component, OnInit } from '@angular/core';
import { SubjectService } from '../services/subject.service';
import { AlertsService } from '../services/alerts.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-chrompack',
  templateUrl: './chrompack.component.html',
  styleUrls: ['./chrompack.component.css']
})
export class ChrompackComponent implements OnInit {

  slots: any;
  selectedId: String;
  title: String;

  constructor(private router: Router,
              private route: ActivatedRoute,
              private alerts: AlertsService,
              private subjectService: SubjectService) {}

  ngOnInit() {

    const idParamRouter = this.route.snapshot.params['id'];

    if (idParamRouter) {
      const chrompackRoute = {_id: idParamRouter};
      this.selectChrompack(chrompackRoute);
    }
    else {
      this.fillSettingsDefault();
    }
  }

  fillSettingsDefault() {
    this.subjectService.getMatrixDefault().subscribe(result => {
      this.slots = result;
    }, err => {
      this.alerts.error('There was an error while displaying slots array', err);
    });
  }

  selectChrompack(chrompack) {

    this.selectedId = chrompack._id;
    this.title = chrompack.title;

    this.subjectService.getMatrixAll(this.selectedId).subscribe(result => {
      this.slots = result;
    }, err => {
      this.alerts.error('There was an error while displaying slots array', err);
    });
  }

  editSubjects(chrompack){
    this.router.navigateByUrl(`chrompack/${chrompack._id}/subject`);
  }

  reset() {
    this.selectedId = null;
    this.fillSettingsDefault();
  }
}
