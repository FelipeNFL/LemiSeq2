import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { Subscription } from 'rxjs';
import { AlertsService } from '../services/alerts.service';
import { ModalConfirmComponent } from '../modal-confirm/modal-confirm.component';

@Component({
  selector: 'chrompack-list',
  templateUrl: './chrompack-list.component.html',
  styleUrls: ['./chrompack-list.component.css']
})
export class ChrompackListComponent implements OnInit {

  @Output() eventSelectChrompack = new EventEmitter();
  @Output() eventEditSubjects = new EventEmitter();
  refreshMetricsSubscription: Subscription;
  chrompacks: Array<any>;
  selectedChrompack: any;

  constructor(private modalService: NgbModal,
              private alerts: AlertsService,
              private chrompackService: ChromPackService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {
    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.getList();
    });

    this.getList();
  }

  select(chrompack) {
    const id = chrompack._id;

    this.chrompacks.forEach(chrompack => {
      chrompack.selected = chrompack._id === id;
    });

    this.selectedChrompack = chrompack;
    this.eventSelectChrompack.emit(this.selectedChrompack);
  }

  editSubjects() {
    this.eventEditSubjects.emit(this.selectedChrompack);
  }

  add() {
    this.modalService.open(UploadComponent);
  }

  getList() {
    this.chrompackService.getList().subscribe(result => {
      this.chrompacks = result;
    }, err => {
      this.alerts.error("There are errors to get chrompack's list in server", err);
    });
  }

  delete() {

    const modalRef = this.modalService.open(ModalConfirmComponent);
    
    modalRef.componentInstance.title = 'DELETE CHROMPACK';
    modalRef.componentInstance.text = `Do you really want to delete the chrompack ${this.selectedChrompack.title}?`;
    modalRef.componentInstance.eventYes.subscribe(() => {
      this.chrompackService.delete(this.selectedChrompack._id).subscribe(() => {
        this.getList();
        this.chrompackServiceObservable.sendRefreshResult();
      }, err => {
        this.alerts.error("There are errors to delete chrompack", err);
      });
    });
  }
}
