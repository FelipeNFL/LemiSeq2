import { Component, OnInit, Output, EventEmitter, Input, ViewChild } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NewSubjectComponent } from '../new-subject/new-subject.component';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { Subscription } from 'rxjs';
import { SubjectService } from '../services/subject.service';
import { Router } from '@angular/router';
import { AlertsService } from '../services/alerts.service';
import { ModalConfirmComponent } from '../modal-confirm/modal-confirm.component';

@Component({
  selector: 'subject-list',
  templateUrl: './subject-list.component.html',
  styleUrls: ['./subject-list.component.css']
})
export class SubjectListComponent implements OnInit {

  @Input() idChrompack: string;
  @Output() eventSelectSubject = new EventEmitter();
  subjects: Array<any>;
  refreshMetricsSubscription: Subscription;
  selected: string;

  constructor(private modalService: NgbModal,
              private alerts: AlertsService,
              private subjectService: SubjectService,
              private router: Router,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {
    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.getList();
    });

    this.getList();
  }

  refreshSelection(title) {
    this.subjects.forEach(subject => { subject.selected = title === subject.title });
  }

  select(subject) {
    this.selected = subject.title;
    this.refreshSelection(this.selected);
    this.eventSelectSubject.emit(this.selected);
  }

  add() {
    const modalRef = this.modalService.open(NewSubjectComponent);
    modalRef.componentInstance.idChrompack = this.idChrompack;
  }

  getList() {
    this.subjectService.getList(this.idChrompack).subscribe(subjects => {
      this.subjects = subjects.map(subject => { return { title: subject, selected: false} });
    }, err => {
      this.alerts.error("There are errors to get subject's list", err);
    });
  }

  delete() {

    const modalRef = this.modalService.open(ModalConfirmComponent);

    modalRef.componentInstance.title = "DELETE SUBJECT";
    modalRef.componentInstance.text = `Do you really want to delete the subject ${this.selected}?`;
    modalRef.componentInstance.eventYes.subscribe(() => {

      this.subjectService.delete(this.idChrompack, this.selected).subscribe(() => {
        this.getList();
        this.chrompackServiceObservable.sendRefreshResult();
      }, err => {
        this.alerts.error("There are errors to delete selected subject", err);
      });
    });
  }

  rename() {
    //TODO abrir modal de renomeação de subject
  }

  back() {
    this.router.navigateByUrl(`chrompack/${this.idChrompack}`);
  }
  view() {
    this.subjectService.build(this.idChrompack,  this.selected).subscribe(() => {
      this.alerts.success('Boa mlk');
    }, err => { this.alerts.error("Errou", err)}  )
  }
}
